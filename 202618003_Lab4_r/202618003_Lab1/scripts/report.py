import pandas as pd

# Read the scraped dataset
df = pd.read_csv("books_raw.csv")

print("=" * 50)
print("TASK 1 REPORT")
print("=" * 50)

print(f"\nTotal Records: {len(df)}")
print(f"Total Columns: {len(df.columns)}")

print("\nColumn Names:")
print(df.columns.tolist())

print("\nMissing Values:")
print(df.isnull().sum())

duplicate_upc = df["UPC"].duplicated().sum()
print(f"\nDuplicate UPC Values: {duplicate_upc}")

print("\nData Types:")
print(df.dtypes)