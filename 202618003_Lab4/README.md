# Airbnb Price Prediction

## DS605: Fundamentals of Machine Learning

This project develops an end-to-end machine learning system for predicting
nightly Airbnb prices using the New York City Airbnb Open Data dataset.

## Project Objective

The objective is to:

- Analyze and clean Airbnb listing data
- Handle missing values and outliers
- Perform feature engineering and preprocessing
- Train and compare regression models
- Tune the best-performing model
- Save the complete machine learning pipeline
- Build a Streamlit application for price prediction

## Dataset

The project uses the Airbnb New York City Open Data (AB_NYC_2019.csv).

The dataset contains information about Airbnb listings including:

- Neighbourhood
- Neighbourhood group
- Latitude and longitude
- Room type
- Minimum nights
- Number of reviews
- Reviews per month
- Host listing count
- Availability
- Price

## Data Preparation

The following preprocessing steps were performed:

- Duplicate records were checked.
- Zero-price listings were removed.
- Extreme price outliers above the 99th percentile were removed.
- Missing `reviews_per_month` values were replaced with 0.
- Review date information was converted into year and month features.
- A `has_review` feature was created.
- Identifier and high-cardinality text columns were removed.

## Models

Three regression models were compared:

1. Linear Regression
2. Random Forest Regression
3. Gradient Boosting Regression

### Initial Results

| Model | MAE | RMSE | R² |
|---|---:|---:|---:|
| Random Forest | 40.53 | 62.33 | 0.5140 |
| Gradient Boosting | 40.89 | 62.58 | 0.5101 |
| Linear Regression | 44.45 | 66.68 | 0.4439 |

Random Forest was selected for further hyperparameter tuning.

## Hyperparameter Tuning

GridSearchCV with 3-fold cross-validation was used.

Best parameters:

- `n_estimators`: 150
- `max_depth`: 15
- `min_samples_split`: 5

## Final Model Performance

The tuned Random Forest achieved:

- MAE: 40.50
- RMSE: 62.24
- R²: 0.5154

## Streamlit Application

A Streamlit application was developed that accepts Airbnb listing information
and predicts the estimated nightly price.

Run the application using:

```bash
streamlit run app.py
