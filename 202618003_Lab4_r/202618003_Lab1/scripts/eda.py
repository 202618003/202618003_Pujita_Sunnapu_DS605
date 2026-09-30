import pandas as pd
import matplotlib.pyplot as plt
from wordcloud import WordCloud

# Load cleaned dataset
df = pd.read_csv("books_cleaned.csv")

print("=" * 50)
print("TASK 3 - EXPLORATORY DATA ANALYSIS")
print("=" * 50)

print("\nSummary Statistics:")
print(df.describe())

# -----------------------
# Plot 1: Price Distribution
# -----------------------
plt.figure(figsize=(6,4))
plt.hist(df["price"], bins=10)
plt.title("Price Distribution")
plt.xlabel("Price (£)")
plt.ylabel("Frequency")
plt.tight_layout()
plt.savefig("price_distribution.png")
plt.close()

# -----------------------
# Plot 2: Rating Distribution
# -----------------------
plt.figure(figsize=(6,4))
df["rating"].value_counts().sort_index().plot(kind="bar")
plt.title("Rating Distribution")
plt.xlabel("Rating")
plt.ylabel("Number of Books")
plt.tight_layout()
plt.savefig("rating_distribution.png")
plt.close()

# -----------------------
# Plot 3: Average Price by Category
# -----------------------
avg_price = (
    df.groupby("category")["price"]
    .mean()
    .sort_values(ascending=False)
)

plt.figure(figsize=(12,5))
avg_price.plot(kind="bar")
plt.title("Average Price by Category")
plt.ylabel("Average Price (£)")
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig("average_price_category.png")
plt.close()

# -----------------------
# Plot 4: Price vs Rating
# -----------------------
plt.figure(figsize=(6,4))
plt.scatter(df["rating"], df["price"])
plt.title("Price vs Rating")
plt.xlabel("Rating")
plt.ylabel("Price (£)")
plt.tight_layout()
plt.savefig("price_vs_rating.png")
plt.close()

# -----------------------
# Word Cloud
# -----------------------
text = " ".join(df["product_description"].astype(str))

wordcloud = WordCloud(
    width=800,
    height=400,
    background_color="white"
).generate(text)

plt.figure(figsize=(10,5))
plt.imshow(wordcloud, interpolation="bilinear")
plt.axis("off")
plt.tight_layout()
plt.savefig("wordcloud.png")
plt.close()

print("\nEDA Completed Successfully!")

print("\nGenerated Files:")
print("- price_distribution.png")
print("- rating_distribution.png")
print("- average_price_category.png")
print("- price_vs_rating.png")
print("- wordcloud.png")