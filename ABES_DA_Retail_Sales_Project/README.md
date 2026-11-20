# Retail Sales Performance Analysis

End-to-end exploratory data analysis (EDA) and KPI reporting on retail sales data using Python, `pandas`, and `matplotlib`.

## Project Structure

- `data/raw/retail_sales.csv` — Raw input dataset
- `data/processed/retail_sales_clean.csv` — Cleaned dataset with engineered features (`Year_Month`, `Profit_Margin_%`)
- `notebooks/retail_sales_analysis.ipynb` — Step-by-step data cleaning, KPI calculation, and visualization notebook
- `scripts/generate_data.py` — Script to generate synthetic sample retail data
- `images/` — Exported charts used for reporting

## Setup & Usage

1. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
2. Place your dataset at `data/raw/retail_sales.csv` (or run `python scripts/generate_data.py` to create sample data).
3. Open and run `notebooks/retail_sales_analysis.ipynb` in Jupyter / VS Code.
