# DS605: Fundamentals of Machine Learning

## Lab Assignment 2 — Vectorized Programming with NumPy and Data Wrangling with Pandas

### Student Information

| Field      | Details                                 |
| ---------- | --------------------------------------- |
| Name       | Pujita Sunnapu                          |
| Student ID | 202618003                               |
| Course     | DS605: Fundamentals of Machine Learning |
| Lab        | Lab Assignment 2                        |
| Dataset    | Kaggle Titanic Dataset (`train.csv`)    |

---

## 1. Assignment Overview

This lab assignment focuses on practicing vectorized programming with NumPy and data wrangling with Pandas using the Titanic dataset.

The assignment covers array operations, statistical analysis, linear algebra, probability distributions, data filtering, grouping, missing-value handling, outlier detection, feature engineering, pivot tables, and visualization.

---

## 2. Objectives

The main objectives of this assignment are to:

* Understand and apply NumPy array operations.
* Perform statistical calculations using NumPy.
* Work with multidimensional arrays.
* Apply vectorized arithmetic and matrix operations.
* Generate and analyze normally distributed data.
* Load and inspect a real-world dataset using Pandas.
* Filter and summarize data based on multiple conditions.
* Handle missing values using different imputation techniques.
* Detect outliers using the IQR method.
* Create new features from existing variables.
* Use grouping and pivot tables to analyze passenger survival.
* Create visualizations and derive observations from the data.

---

## 3. Repository Contents

| File / Folder              | Description                                                           |
| -------------------------- | --------------------------------------------------------------------- |
| `Lab_2_NumPy_Pandas.ipynb` | Complete Jupyter Notebook containing the assignment code and analysis |
| `train.csv`                | Titanic dataset used for the Pandas tasks                             |
| `README.md`                | Project documentation                                                 |

> **Note:** Update the filenames above if the actual filenames in the repository are different.

---

## 4. Part A — Vectorized Programming with NumPy

### Task 1 — Arrays, Statistics, and Indexing

* Generated a reproducible random array containing 100 integers.
* Calculated the minimum, maximum, median, mean, and standard deviation.
* Created an array containing exactly 100 values using `np.arange()`.
* Demonstrated `np.zeros()` and `np.ones()`, including their shape and data type.
* Demonstrated `np.linspace()` and compared it with `np.arange()`.
* Created and explored 2D and 3D arrays.
* Demonstrated array shape, dimensions, indexing, rows, columns, and slicing.
* Used `reshape()` to create a matrix and `flatten()` to convert it back to one dimension.

### Task 2 — Vectorized Arithmetic and Linear Algebra

* Performed matrix addition.
* Performed element-wise multiplication.
* Performed matrix multiplication using the `@` operator.
* Calculated the transpose of a square matrix.
* Calculated the determinant of a square matrix.
* Calculated the inverse when the matrix was invertible.
* Verified the inverse using `np.allclose()`.

### Task 3 — Normal Distribution and Histogram

* Generated 1,000 observations from a normal distribution.
* Used a chosen mean of 50 and standard deviation of 10.
* Calculated the sample mean and sample standard deviation.
* Compared the sample statistics with the chosen distribution parameters.
* Visualized the generated distribution using a histogram.

---

## 5. Part B — Titanic Data Wrangling with Pandas

### Task 4 — Load and Inspect Data

* Loaded the Titanic `train.csv` dataset using Pandas.
* Examined the first and last rows using `head()` and `tail()`.
* Checked the dataset shape and column names.
* Inspected data types and non-null values using `info()`.
* Generated descriptive statistics using `describe()`.
* Demonstrated row and column selection using both `loc` and `iloc`.

### Task 5 — Filtering and Querying

Boolean indexing was used to answer questions involving:

* Male passengers older than 50.
* Female first-class passengers and their survival percentage.
* Passengers aged 20–40 with fares above the overall median who survived.
* Passengers travelling alone, younger than 30, who did not survive.
* Passengers who embarked at Southampton, travelled in second or third class, and paid a fare above the Southampton median.

### Task 6 — Groupby and Aggregation

The Titanic dataset was grouped to calculate:

* Survival rate by sex.
* Survival rate by passenger class.
* Average age and fare by passenger class.
* Passenger count and survival rate by sex and passenger class.
* Passenger count, average fare, and survival rate by embarkation point.

### Task 7 — Missing Values and Fare Outliers

* Calculated missing-value counts and percentages for every column.
* Visualized missing-value counts using a bar chart.
* Filled missing `Age` values using mean imputation.
* Compared mean, median, mode, and random-value imputation approaches.
* Calculated Q1, Q3, and IQR for `Fare`.
* Calculated the lower and upper 1.5 × IQR bounds.
* Counted the observations identified as Fare outliers.

### Task 8 — Feature Engineering and Pivot Table

Two new features were created:

* `FamilySize = SibSp + Parch + 1`
* `IsAlone = 1` when `FamilySize = 1`, otherwise `0`

A pivot table was also created with:

* Rows: `Sex`
* Columns: `Pclass`
* Values: mean `Survived`

The highest and lowest survival-rate groups were identified from the resulting pivot table.

### Task 9 — Visualizations and Observations

Three main visualizations were created:

1. Correlation heatmap for relevant numerical variables.
2. Survival rate by sex.
3. Age vs Fare, distinguished by survival status.

These visualizations, together with the numerical analyses from the previous tasks, were used to identify patterns in the Titanic dataset.

---

## 6. Key Observations

### 1. Survival differed substantially by sex

Female passengers had a survival rate of approximately **74.20%**, compared with **18.89%** for male passengers. This represents a difference of approximately **55.31 percentage points**, showing a strong association between sex and survival outcomes in the Titanic dataset.

### 2. Passenger class was associated with survival

The correlation between `Pclass` and `Survived` was approximately **-0.34**. Since lower numerical values represent higher passenger classes, this negative relationship is consistent with higher-class passengers generally having better survival outcomes.

### 3. Sex and passenger class together showed strong differences in survival

The `Sex × Pclass` pivot table showed substantial differences between groups. The highest survival rate was observed among **female first-class passengers at 96.81%**, while the lowest was observed among **male third-class passengers at 13.54%**.

This demonstrates that examining sex and passenger class together provides more detailed information about survival than considering either variable alone.

### 4. Fare and passenger class had a moderately strong negative relationship

The correlation between `Pclass` and `Fare` was approximately **-0.55**. This is consistent with the coding of passenger class, where `1` represents first class and `3` represents third class. Therefore, passengers in higher classes generally paid higher fares.

### 5. Fare had a positive relationship with survival

The correlation between `Fare` and `Survived` was approximately **0.26**. This indicates a positive but relatively weak relationship, suggesting that passengers paying higher fares tended to have somewhat higher survival rates, although Fare alone does not explain survival outcomes.

### 6. Family-related variables showed strong relationships

`SibSp` and `FamilySize` had a strong positive correlation of approximately **0.89**, while `FamilySize` and `IsAlone` had a negative correlation of approximately **-0.69**.

These strong relationships are expected because `FamilySize` and `IsAlone` were directly engineered from the family-related variables.

### 7. Age and Fare did not completely separate survivors from non-survivors

The Age vs Fare scatter plot showed substantial overlap between surviving and non-surviving passengers across different ages and fare levels. Although some patterns are visible, Age and Fare alone do not completely distinguish between the two survival groups. The plot also shows a small number of passengers with exceptionally high fares.

---

## 7. Technologies and Libraries

The assignment was implemented using Python and the following libraries:

* **NumPy** — numerical computing, arrays, statistics, random sampling, and linear algebra.
* **Pandas** — data loading, filtering, grouping, aggregation, missing-value handling, and feature engineering.
* **Matplotlib** — data visualization.
* **Seaborn** — correlation heatmap visualization.
* **Jupyter Notebook** — development and execution environment.

---

## 8. Key Concepts Practiced

The main concepts demonstrated in this lab include:

### NumPy

* Array creation
* Random number generation
* Statistical functions
* Indexing and slicing
* Reshaping and flattening
* Vectorized arithmetic
* Element-wise vs matrix multiplication
* Matrix transpose
* Determinant and inverse
* Normal distribution

### Pandas

* DataFrame creation and loading
* Dataset inspection
* `loc` and `iloc`
* Boolean indexing
* `query()`
* `groupby()`
* Aggregation
* Missing-value detection and imputation
* IQR-based outlier detection
* Feature engineering
* Pivot tables

### Visualization

* Histograms
* Bar charts
* Scatter plots
* Correlation heatmaps
