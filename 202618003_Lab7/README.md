# Image Representation, PCA, Eigenfaces and Face Recognition

**Course:** DS605 — Fundamentals of Machine Learning  
**Assignment:** Lab Assignment 7

## Objective

Represent face images numerically, implement PCA using NumPy linear algebra,
visualize eigenfaces, reconstruct images, perform face recognition, and compare
similarity-based matching with traditional machine-learning classifiers.

## Dataset

This project uses the AT&T Database of Faces (ORL).

- Images loaded: 400
- Subjects: 40
- Images per subject: 10
- Image dimensions: 112 × 92
- Original pixel features per image: 10304

Place the extracted dataset under `data/archive/`, with subject folders such
as `s1`, `s2`, and so on.

## Methodology

1. Load grayscale PGM images and extract subject labels.
2. Flatten images into pixel feature vectors.
3. Create a reproducible, subject-stratified train-test split.
4. Compute the mean face and center the data.
5. Implement covariance-based eigendecomposition using a smaller Gram matrix.
6. Implement PCA independently using NumPy SVD.
7. Compare eigenvalues and principal directions from both methods.
8. Select components using cumulative explained variance.
9. Visualize eigenfaces and reconstruct test images.
10. Compare raw-pixel and PCA-space nearest-neighbor recognition.
11. Train KNN and SVM classifiers on PCA features.
12. Compare component counts using training cross-validation.

PCA calculations use NumPy linear-algebra operations rather than
scikit-learn's PCA implementation.

## Train-Test Split

Each subject contributes 7 training images and 3 test images.

- Training images: 280
- Test images: 120
- Random seed: 42

## PCA Results

- Components selected for at least 90% variance: 92
- Cumulative explained variance: 90.0366%
- Test reconstruction MSE: 335.5241
- Test reconstruction RMSE: 18.3173

## Recognition Results

| Method | Features | Test Accuracy |
|---|---:|---:|
| Nearest Neighbor — Raw Pixels | 10304 | 97.50% |
| Nearest Neighbor — PCA | 92 | 97.50% |
| KNN (k=1) — PCA | 92 | 97.50% |
| SVM (linear) — PCA | 92 | 95.00% |

These results correspond to the specified random split and should not be
interpreted as a guarantee of performance on other datasets.

## Figures

- `outputs/explained_variance.png`
- `outputs/eigenfaces.png`
- `outputs/reconstruction_comparison.png`

## Results Tables

The `outputs/` directory also contains CSV files for explained variance,
eigendecomposition versus SVD, storage comparison, classifier cross-validation,
component-count experiments, and final recognition comparisons.

## Requirements

- Python 3
- NumPy
- Pandas
- Matplotlib
- Pillow
- scikit-learn
- Jupyter Notebook

## Run the Project

1. Clone or download this repository.
2. Install the required packages.
3. Place the extracted ORL dataset under `data/archive/`.
4. Open the notebook in Jupyter.
5. Run the cells from top to bottom.

## Limitations

PCA maximizes variance preservation rather than class separation. The dataset is
small, and results depend on the train-test split. The PCA model also requires
storage for the mean face and principal directions, which matters when evaluating
total storage on a small dataset.
