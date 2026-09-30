# DS605 Lab Assignment 1
## Data Scraping and Preprocessing using Python and Scrapy

### Student Details

- **Name:** Pujita Sunnapu
- **Student ID:** 202618003

---

## Objective

The objective of this assignment is to build a complete data pipeline by scraping book information from **https://books.toscrape.com/** using Scrapy, preprocessing the collected data, performing exploratory data analysis, generating visualizations, and extracting meaningful insights.

---

## Project Structure

```
202618003_Lab1
│
├── bookscraper/
│   ├── spiders/
│   │   └── books.py
│   ├── settings.py
│   └── scrapy.cfg
│
├── scripts/
│   ├── report.py
│   ├── preprocess.py
│   └── eda.py
│
├── books_raw.csv
├── books_cleaned.csv
├── price_distribution.png
├── rating_distribution.png
├── average_price_category.png
├── price_vs_rating.png
├── wordcloud.png
├── INSIGHTS.md
├── README.md
└── scrapy.cfg
```

---

## Task 1 – Data Scraping

- Scraped **100 books** from the first five catalogue pages.
- Extracted:
  - Title
  - Category
  - Price
  - Rating
  - Availability
  - Product Description
  - UPC
  - Number of Reviews
  - Product URL
- Exported the scraped data to `books_raw.csv`.

---

## Task 2 – Data Preprocessing

The following preprocessing steps were performed:

- Removed duplicate books using UPC.
- Cleaned whitespace and inconsistent text.
- Handled missing descriptions.
- Converted price to numeric values.
- Converted ratings from One–Five to integers.
- Extracted stock count.

### Engineered Features

- `stock_count`
- `description_word_count`
- `price_category`
- `is_popular`

The cleaned dataset was saved as `books_cleaned.csv`.

---

## Task 3 – Visualization and Analysis

Generated visualizations:

- Price Distribution
- Rating Distribution
- Average Price by Category
- Price vs Rating
- Word Cloud from Book Descriptions

Summary statistics were also generated for the cleaned dataset.

---

## Technologies Used

- Python
- Scrapy
- Pandas
- Matplotlib
- WordCloud

---

## How to Run

### 1. Scrape the data

```bash
scrapy crawl books -O books_raw.csv
```

### 2. Generate Task 1 report

```bash
python scripts/report.py
```

### 3. Preprocess the data

```bash
python scripts/preprocess.py
```

### 4. Perform EDA

```bash
python scripts/eda.py
```

---

## Output Files

- `books_raw.csv`
- `books_cleaned.csv`
- `price_distribution.png`
- `rating_distribution.png`
- `average_price_category.png`
- `price_vs_rating.png`
- `wordcloud.png`
- `INSIGHTS.md`

---

## Assignment Status

- ✅ Task 1 – Data Scraping
- ✅ Task 2 – Data Preprocessing
- ✅ Task 3 – Visualization and Analysis
- ✅ Task 4 – Insights and Interpretation