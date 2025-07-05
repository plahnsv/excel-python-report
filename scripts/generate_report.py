import pandas as pd
import os

# --- Config ---
input_file = os.path.join("data", "input_data.csv")
output_file = os.path.join("output", "processed_report.xlsx")

# --- Load ---
df = pd.read_csv(input_file)

# --- Clean ---
df['Date'] = pd.to_datetime(df['Date'])
df = df.sort_values(['Well', 'Date'])

# --- Fill missing monthly dates per Well ---
def fill_missing_dates(group):
    all_months = pd.date_range(start=group['Date'].min(),
                               end=group['Date'].max(),
                               freq='M')
    group = group.set_index('Date').reindex(all_months)
    group.index.name = 'Date'
    group['Well'] = group['Well'].ffill()
    group[['Oil_Rate', 'Water_Rate', 'Gas_Rate']] = group[['Oil_Rate', 'Water_Rate', 'Gas_Rate']].fillna(0)
    return group.reset_index()

df_filled = df.groupby('Well').apply(fill_missing_dates).reset_index(drop=True)

# --- Save to Excel ---
df_filled.to_excel(output_file, index=False)
print(f"Report saved to: {output_file}")

