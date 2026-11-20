from pathlib import Path
import numpy as np
import pandas as pd


def main():
    rng = np.random.default_rng(42)
    n_rows = 500

    dates = pd.date_range("2025-01-01", "2025-12-31", periods=n_rows)
    categories = ["Electronics", "Clothing", "Home & Kitchen", "Groceries", "Sports"]
    regions = ["North", "South", "East", "West"]

    quantities = rng.integers(1, 8, size=n_rows)
    unit_prices = np.round(rng.uniform(15.0, 450.0, size=n_rows), 2)
    sales = np.round(quantities * unit_prices, 2)
    margins = rng.uniform(0.08, 0.35, size=n_rows)
    profit = np.round(sales * margins, 2)

    df = pd.DataFrame({
        "Order_ID": [f"ORD-{1000 + i}" for i in range(n_rows)],
        "Order_Date": rng.choice(dates, size=n_rows),
        "Category": rng.choice(categories, size=n_rows),
        "Region": rng.choice(regions, size=n_rows),
        "Quantity": quantities,
        "Unit_Price": unit_prices,
        "Sales": sales,
        "Profit": profit,
    })

    out_path = Path(__file__).resolve().parent.parent / "data" / "raw" / "retail_sales.csv"
    out_path.parent.mkdir(parents=True, exist_ok=True)
    df.to_csv(out_path, index=False)
    print(f"Generated sample dataset at: {out_path}")


if __name__ == "__main__":
    main()
