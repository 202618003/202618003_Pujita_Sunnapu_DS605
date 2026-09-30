import pandas as pd
import re

# Load dataset
df = pd.read_csv("books_raw.csv")

# -----------------------------
# 1. Remove duplicate books
# -----------------------------
df.drop_duplicates(subset="UPC", inplace=True)

# -----------------------------
# 2. Handle missing values
# -----------------------------
df["product_description"] = df["product_description"].fillna("No Description")

# -----------------------------
# 3. Clean whitespace
# -----------------------------
text_columns = [
    "title",
    "category",
    "availability",
    "product_description"
]

for col in text_columns:
    df[col] = df[col].str.strip()

# -----------------------------
# 4. Convert price to float
# -----------------------------
df["price"] = (
    df["price"]
    .replace("£", "", regex=True)
    .astype(float)
)

# -----------------------------
# 5. Convert ratings to numbers
# -----------------------------
rating_map = {
    "One": 1,
    "Two": 2,
    "Three": 3,
    "Four": 4,
    "Five": 5
}

df["rating"] = df["rating"].map(rating_map)

# -----------------------------
# 6. Extract stock quantity
# -----------------------------
df["stock_count"] = df["availability"].str.extract(r"(\d+)").astype(int)

# =============================
# Create New Features
# =============================

# Feature 1
df["description_word_count"] = (
    df["product_description"]
    .str.split()
    .str.len()
)

# Feature 2
df["price_category"] = pd.cut(
    df["price"],
    bins=[0, 15, 30, 60],
    labels=["Low", "Medium", "High"]
)

# Feature 3
df["is_popular"] = (
    df["rating"] >= 4
).astype(int)

# Save cleaned dataset
df.to_csv("books_cleaned.csv", index=False)

print("=" * 50)
print("TASK 2 COMPLETED")
print("=" * 50)

print("\nRows:", len(df))
print("Columns:", len(df.columns))

print("\nNew Features Added:")
print("- stock_count")
print("- description_word_count")
print("- price_category")
print("- is_popular")

print("\nCleaned dataset saved as books_cleaned.csv")