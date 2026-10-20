import numpy as np
import pandas as pd
import os

def load_data(path):
  return pd.read_csv(path)

def clean_data(df):
    df['Units Sold'] = pd.to_numeric(df['Units Sold'], errors="coerce")
    df['Total Sales'] = pd.to_numeric(df['Total Sales'], errors="coerce")

    df['Units Sold'] = df['Units Sold'].fillna(df['Units Sold'].mean())
    df['Total Sales'] = df['Total Sales'].fillna(df['Total Sales'].mean())

    df.columns = df.columns.str.strip()

    df['Date'] = pd.to_datetime(df['Date'], errors="coerce")

    for col in ['Region', 'Product', 'Category']:
        df[col] = df[col].str.strip().str.title()

    df['Units Sold'] = pd.to_numeric(df['Units Sold'], errors="coerce")

    for col in ['Unit Price', 'Total Sales']:
        df[col] = df[col].astype(str)
        df[col] = df[col].str.replace("[$,USD]", "", regex=True).str.strip()
        df[col] = pd.to_numeric(df[col], errors="coerce")

    df['Profit Margin (%)'] = (
        df['Profit Margin (%)']
        .astype(str)
        .str.replace("%", "", regex=True)
        .str.replace("percent", "", regex=True)
        .astype(float)
    )
    df['Profit Margin (%)'] = np.where(
        df['Profit Margin (%)'] < 1,
        df['Profit Margin (%)'] * 100,
        df['Profit Margin (%)']
    )

    df_cleaned = df.dropna(subset=["Date", "Total Sales", "Region"])
    return df_cleaned

def inspect_dataset(df):
    print("--- DataFrame Info ---")
    df.info()
    print("\n--- Missing Values Count ---")
    print(df.isnull().sum())

def analyze_data_numpy(df_cleaned):
    units = df_cleaned['Units Sold'].to_numpy(dtype=np.float64)
    prices = df_cleaned['Unit Price'].to_numpy(dtype=np.float64)
    margins = df_cleaned['Profit Margin (%)'].to_numpy(dtype=np.float64) / 100.0

    calculated_sales = units * prices
    estimated_profit = calculated_sales * margins

    metrics = {
        "total_revenue": np.sum(calculated_sales),
        "mean_revenue": np.mean(calculated_sales),
        "median_revenue": np.median(calculated_sales),
        "std_revenue": np.std(calculated_sales),
        "total_estimated_profit": np.sum(estimated_profit),
        "p90_revenue": np.percentile(calculated_sales, 90)
    }

    high_value_mask = calculated_sales >= metrics["p90_revenue"]
    metrics["top_orders_count"] = np.count_nonzero(high_value_mask)

    return metrics

def save_data(df_cleaned, path):
  directory = os.path.dirname(path)
  if directory and not os.path.exists(directory):
      os.makedirs(directory, exist_ok=True)

  df_cleaned.to_csv(path, index=False)

df_raw = load_data("messy_sales.csv")

df_cleaned = clean_data(df_raw)

results = analyze_data_numpy(df_cleaned)

save_data(df_cleaned, "cleaned_sales.csv")

for metric, value in results.items():
    print(f"{metric:<25}: {value:,.2f}")