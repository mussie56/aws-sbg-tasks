# Small Python Data-Processing App

A lightweight, reproducible data-processing pipeline that ingests raw retail sales data, cleans and standardizes inconsistent records using **Pandas**, computes key financial metrics with **NumPy**, and exports the clean dataset for downstream analysis.

---

## Features

- **Raw Ingestion**: Loads uncleaned tabular sales data (`messy_sales.csv`).
- **Functional Cleaning (Pandas)**:
  - Normalizes text and categorical columns (Region, Product, Category).
  - Handles missing values (`NaN`) and text representation of numbers.
  - Cleans messy currency strings and formats percentage margins.
  - Recomputes and validates total sales values.
- **Numerical Analytics (NumPy)**:
  - Converts Pandas series to contiguous NumPy float arrays.
  - Computes vectorized financial metrics: Gross Revenue, Gross Profit, and COGS.
  - Calculates summary statistics (mean, median, std dev, 90th percentile).
- **Export Utility**: Exports cleaned results directly to CSV, Excel, or Parquet.

---

## Project Structure

```text
├── data/
│   ├── messy_sales.csv       # Raw input dataset
│   └── cleaned_sales.csv     # Exported clean dataset
├── notebooks/
│   └── data_cleaning.ipynb   # Interactive analysis notebook
├── requirements.txt          # Python dependencies
└── README.md                 # Project documentation
