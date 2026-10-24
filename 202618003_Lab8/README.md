# DS605 Lab Assignment 8: Decision Trees and Support Vector Machines

## Overview

This assignment implements and evaluates Decision Tree and Support
Vector Machine (SVM) classifiers using the Banknote Authentication
dataset. It includes from-scratch implementations, comparisons with
Scikit-learn, decision-boundary visualizations, and experiments with
nonlinear SVM kernels.

## Objectives

-   Implement Gini impurity and entropy.
-   Build a Decision Tree classifier from scratch using recursive
    splitting.
-   Implement a linear soft-margin SVM using NumPy and subgradient
    descent.
-   Compare manual implementations with Scikit-learn models.
-   Visualize decision boundaries.
-   Investigate tree depth, split criterion, regularization, learning
    rate, and iteration count.
-   Compare linear, polynomial, and RBF SVM kernels.
-   Evaluate final models using all four dataset features.

## Dataset

**Banknote Authentication dataset**

Expected file path: `data/data_banknote_authentication.txt`

The comma-separated text file has no header row. The notebook assigns
these columns:

1.  `variance`
2.  `skewness`
3.  `curtosis`
4.  `entropy`
5.  `class` (target)

The loaded dataset contains 1,372 rows and 5 columns, with no missing
values. Class distribution:

-   Class 0: 762 samples
-   Class 1: 610 samples

## Project structure

``` text
202618003_Lab8/
├── README.md
├── data/
│   └── data_banknote_authentication.txt
└── <notebook>.ipynb
```

Replace `<notebook>.ipynb` with the actual name of the completed
notebook.

## Requirements

-   Python 3
-   NumPy
-   pandas
-   Matplotlib
-   scikit-learn
-   Jupyter Notebook or the VS Code Jupyter extension

Install packages if needed:

``` bash
pip install numpy pandas matplotlib scikit-learn jupyter
```

## How to run

1.  Open the project folder in VS Code or Jupyter.
2.  Confirm that `data/data_banknote_authentication.txt` exists.
3.  Open the completed notebook and select a Python environment with the
    required packages.
4.  Restart the kernel and run all cells from top to bottom.
5.  Review the plots, metric tables, and confusion matrix.

The banknote dataset uses a stratified 80:20 train-test split with
`random_state=42`. Two-feature experiments use `variance` and `skewness`
for visualization. The final comparison uses all four features. SVM
features are standardized using training-set statistics only.

## Assignment workflow

### Part A --- Decision Tree from scratch

-   Implement Gini impurity and entropy.
-   Find the best feature-threshold split.
-   Build the tree recursively with stopping conditions.
-   Evaluate predictions with accuracy, precision, recall, and F1-score.
-   Visualize the tree and decision boundary.
-   Compare with Scikit-learn and study criteria and maximum depth.

### Part B --- Linear SVM from scratch

-   Standardize features and encode labels as -1 and +1.
-   Implement a linear soft-margin SVM using hinge loss and subgradient
    descent.
-   Plot objective history, decision boundary, margins, and margin
    violations.
-   Compare with Scikit-learn.
-   Experiment with `C`, learning rate, and iteration count.

### Part C --- Kernel SVM

-   Generate a nonlinear `make_moons` dataset.
-   Compare linear, degree-3 polynomial, and RBF kernels.
-   Visualize decision boundaries.
-   Investigate the effect of `C` on RBF SVM performance.

### Part D --- Final four-feature comparison

Compare the manual Decision Tree, Scikit-learn Decision Tree, manual
Linear SVM, Scikit-learn Linear SVM, polynomial SVM, and RBF SVM on the
full four-feature banknote dataset. Report accuracy, precision, recall,
F1-score, training time, and prediction time. Generate a confusion
matrix for the RBF SVM.

## Results observed

The following results came from the recorded notebook run on the
275-sample banknote test set using all four features. Timing varies by
computer and runtime environment.

  Model                          Accuracy   Precision   Recall   F1-score
  ---------------------------- ---------- ----------- -------- ----------
  Scikit-learn RBF SVM             1.0000      1.0000   1.0000     1.0000
  Manual Decision Tree             0.9927      0.9839   1.0000     0.9919
  Scikit-learn Decision Tree       0.9927      0.9839   1.0000     0.9919
  Polynomial SVM (degree 3)        0.9818      0.9606   1.0000     0.9799
  Scikit-learn Linear SVM          0.9745      0.9457   1.0000     0.9721
  Manual Linear SVM                0.8800      0.9238   0.7951     0.8546

The RBF SVM confusion matrix showed 153 correctly classified Class 0
samples and 122 correctly classified Class 1 samples, with no errors on
this particular test split.

On the synthetic `make_moons` test set, the RBF kernel achieved 96.50%
accuracy, compared with 91.50% for the linear kernel and 90.50% for the
degree-3 polynomial kernel in the recorded experiment.

**Note:** These results describe one fixed train-test split and do not
guarantee performance on unseen data. The manual SVM and Scikit-learn
SVM use different optimization procedures, so their results need not
match exactly.

## Evaluation metrics

-   **Accuracy:** Fraction of all test predictions that are correct.
-   **Precision:** Fraction of predicted positive-class samples that are
    actually positive.
-   **Recall:** Fraction of actual positive-class samples correctly
    identified.
-   **F1-score:** Harmonic mean of precision and recall.
-   **Training time:** Time measured to fit a model in the current
    runtime.
-   **Prediction time:** Time measured to generate predictions in the
    current runtime.

## Notes

-   Run the notebook from the project folder so the relative dataset
    path resolves correctly.
-   Timing varies with hardware, Python version, package versions, and
    system load.
-   The perfect RBF SVM score applies only to the recorded test split.
    Further validation is needed to assess generalization.
