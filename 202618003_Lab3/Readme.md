# DS605: Fundamentals of Machine Learning

## Lab Assignment 3 — Scikit-learn: Data Preprocessing and Model Performance Evaluation

### Student Information

| Field          | Details                                 |
| -------------- | --------------------------------------- |
| **Name**       | Pujita Sunnapu                          |
| **Student ID** | 202618003                               |
| **Course**     | DS605: Fundamentals of Machine Learning |
| **Lab**        | Lab Assignment 3                        |
| **Dataset**    | Hotel Booking Demand                    |

---

## 1. Assignment Overview

This assignment focuses on data preprocessing and classification model evaluation using **Scikit-learn**.

The **Hotel Booking Demand** dataset contains booking information for city and resort hotels. The objective of this assignment is to predict whether a hotel booking will be canceled using `is_canceled` as the target variable.

Two preprocessing approaches and two classification models are compared:

* StandardScaler vs. MinMaxScaler
* Logistic Regression vs. Decision Tree

All experiments use the same train-test split to ensure a fair comparison.

---

## 2. Dataset

**Dataset:** Hotel Booking Demand

**Source:** Kaggle — Jesse Mostipak

**Dataset Link:** https://www.kaggle.com/datasets/jessemostipak/hotel-booking-demand

The original dataset contains **119,390 rows and 32 columns**.

The target variable is:

* `is_canceled = 0` → Booking was not canceled
* `is_canceled = 1` → Booking was canceled

The original class distribution was:

* Not canceled: **75,166 (62.96%)**
* Canceled: **44,224 (37.04%)**

---

## 3. Data Preprocessing

### Missing Values

Missing values were examined for every column.

The `company` column had approximately **94.31% missing values**, so it was removed because retaining a feature with such a high proportion of missing values would provide limited useful information.

Other columns with smaller amounts of missing data were retained and handled through the preprocessing pipelines.

### Data Leakage

The following columns were removed because they directly reveal the final booking outcome:

* `reservation_status`
* `reservation_status_date`

This prevents information about the final reservation outcome from leaking into the model during training.

### Outliers

Selected numerical variables were examined using boxplots and the IQR method.

Only clear/extreme outliers were removed rather than removing every statistical IQR outlier. A total of **14 rows** were removed.

The resulting dataset contained **119,376 rows** for modeling.

---

## 4. Preprocessing Pipelines

The data was split using:

```text
test_size = 0.2
stratify = y
random_state = 42
```

This resulted in:

* Training set: **95,500 rows**
* Testing set: **23,876 rows**

### Numerical Features

Missing numerical values were handled using:

```text
KNNImputer(n_neighbors=5)
```

Two alternatives were then compared:

**Pipeline A**

```text
KNNImputer → StandardScaler
```

**Pipeline B**

```text
KNNImputer → MinMaxScaler
```

### Categorical Features

Categorical missing values were handled using:

```text
SimpleImputer(strategy="most_frequent")
```

Categorical variables were then transformed using:

```text
OneHotEncoder(handle_unknown="ignore")
```

`ColumnTransformer` and `Pipeline` were used so that preprocessing was fitted only on the training data.

---

## 5. Classification Models

Two classification algorithms were evaluated with both preprocessing pipelines:

1. `LogisticRegression(max_iter=1000)`
2. `DecisionTreeClassifier(random_state=42)`

This resulted in four model-pipeline combinations.

---

## 6. Model Performance

| Model-Pipeline                       | Training Accuracy | Testing Accuracy | Precision |     Recall |   F1-Score |
| ------------------------------------ | ----------------: | ---------------: | --------: | ---------: | ---------: |
| Logistic Regression + StandardScaler |            81.92% |           81.61% |    80.57% |     66.36% |     72.78% |
| Logistic Regression + MinMaxScaler   |            81.54% |           81.16% |    80.04% |     65.44% |     72.01% |
| Decision Tree + StandardScaler       |            99.60% |       **85.99%** |    80.76% | **81.60%** | **81.18%** |
| Decision Tree + MinMaxScaler         |            99.60% |           85.94% |    80.67% |     81.59% |     81.13% |

---

## 7. Final Observations

1. **Decision Tree + StandardScaler gives the best overall result**, achieving the highest testing accuracy of **85.99%** and the highest F1-score of **81.18%** among the four experiments.

2. **StandardScaler performs better than MinMaxScaler for Logistic Regression.** Testing accuracy increases from **81.16% to 81.61%**, while F1-score increases from **72.01% to 72.78%**.

3. **Scaling has very little effect on the Decision Tree.** The testing accuracy is **85.99%** with StandardScaler and **85.94%** with MinMaxScaler, showing only a 0.05 percentage-point difference.

4. **The Decision Tree shows substantial overfitting.** Its training accuracy is **99.60%**, compared with **85.99%** on the test set, producing a train-test gap of approximately **13.62 percentage points**. Logistic Regression has much smaller gaps of approximately **0.31–0.38 percentage points**.

5. **The confusion matrices show that the Decision Tree identifies more canceled bookings correctly.** The best Decision Tree correctly classified **7,216 canceled bookings**, compared with **5,868** for the best Logistic Regression. This contributes to its higher recall and F1-score.

---

## 8. Conclusion

Among the four experiments, **Decision Tree + StandardScaler** provides the strongest test-set performance. However, its substantially higher training accuracy compared with testing accuracy indicates overfitting.

Logistic Regression provides lower overall predictive performance but has a much smaller train-test gap, indicating more consistent generalization. StandardScaler performs slightly better than MinMaxScaler for Logistic Regression, while scaling has almost no effect on the Decision Tree.

The notebook contains the complete preprocessing, model training, evaluation, comparison table, and required confusion matrices.

