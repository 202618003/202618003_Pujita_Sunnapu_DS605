# Insights and Interpretation

## Observations

1. A total of **100 books** were successfully scraped from the first five catalogue pages of the Books to Scrape website.

2. The dataset contains **no missing values** and **no duplicate UPC values**, indicating that the scraping and preprocessing steps were successful.

3. Most books have ratings between **3 and 5 stars**, suggesting that the majority of books listed have positive ratings.

4. The average price varies across different book categories, showing that some categories are generally more expensive than others.

5. The scatter plot of **Price vs Rating** indicates that there is **no strong relationship** between the price of a book and its rating.

6. The generated word cloud highlights the most frequently occurring words in the book descriptions, providing an overview of common themes.

7. The engineered features such as **stock_count**, **price_category**, **description_word_count**, and **is_popular** make the dataset more useful for further analysis and machine learning tasks.

---

## Limitations

- Only the **first five catalogue pages (100 books)** were scraped.
- The dataset comes from a **demo website**, so it may not represent real-world book markets.
- Customer review text is not available; therefore, the text analysis is based only on the product descriptions.
- The analysis is limited to the information available on the website and does not include external data sources.