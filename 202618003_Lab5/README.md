
# DS605 Lab 5 — Machine Learning with Scikit-learn and From Scratch

## Overview

This project implements regression and classification models using two approaches:

1. Scikit-learn
2. From-scratch implementation using NumPy and Pandas

The UCI Productivity Prediction of Garment Employees dataset is used.

## Tasks

### Regression

Predict `actual_productivity` using Linear Regression.

### Classification

Predict whether actual productivity meets the target:

`MeetsTarget = 1` if:

`actual_productivity >= targeted_productivity`

otherwise:

`MeetsTarget = 0`

`actual_productivity` is not used as an input feature for classification.

## Implementation

### Scikit-learn

The Scikit-learn implementation includes:

- Missing-value imputation
- One-hot encoding
- Feature scaling
- Linear Regression
- Logistic Regression
- Evaluation metrics
- Training and prediction timing

### From Scratch

The manual implementation uses only NumPy and Pandas for:

- Missing-value handling
- Categorical encoding
- Feature scaling
- Linear Regression
- Logistic Regression
- Sigmoid function
- Gradient descent
- Prediction
- Evaluation metrics

The same fixed train-test split is used for both implementations.

## Optimization

The manual Logistic Regression was optimized by tuning:

- Learning rate
- Number of gradient-descent iterations

The final optimized configuration uses:

- Learning rate: 0.1
- Iterations: 1,000

This reduced manual Logistic Regression training time by approximately 88% while maintaining the observed F1-score.

## Results

The notebook contains complete comparison tables for:

- MAE
- RMSE
- R²
- Accuracy
- Precision
- Recall
- F1-score
- Training time
- Prediction time

## How to Run

Install the required packages:

```bash
pip install -r requirements.txt
