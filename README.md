Python + Excel reporting template (fill missing dates, output clean report)

# Excel + Python Reporting Template

This project demonstrates how to use Python to process time-series production data (e.g., from oil & gas wells) and output a clean Excel report.

## 🗂 Structure

- 'data/input_data.csv': Input file (Well, Date, Oil_Rate, Water_Rate, Gas_Rate)
- 'scripts/generate_report.py': Python script to fill missing dates and zero-fill missing values
- 'output/processed_report.xlsx': Auto-generated output
- 'templates/': Optional Excel templates (charts, formatting)

## 🚀 How to Run

1. Install dependencies:
pip install -r requirements.txt

2. Run the script:
python scripts/generate_report.py

3. Open the resulting Excel file:
output/processed_report.xlsx

