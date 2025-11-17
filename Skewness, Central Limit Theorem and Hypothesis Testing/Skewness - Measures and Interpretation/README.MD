# Skewness - Measures and Interpretation

## Overview

Skewness is a key statistical measure that shows how data is spread out in a dataset. It tells us if the data points are skewed to the left (negative skew) or to the right (positive skew) in relation to the mean. It is important because it helps us to understand the shape of the data distribution which is important for accurate data analysis and helps in identifying outliers and finding the best statistical methods to use for analysis.

## Types of Skewness

Skewness describes the direction and degree of asymmetry in a dataset's distribution.

### 1\. Positive Skewness (Right Skew)

In a positively skewed distribution, the right tail is longer than the left which means most data points are on the left with a few large values pulling the distribution to the right.

**Relationship:**

` Mean > Median > Mode `

**Examples:** Income distribution, exam scores and stock market returns.

### 2\. Negative Skewness (Left Skew)

In a negatively skewed distribution, the left tail is longer which means most data points are on the right with a few smaller values pulling the distribution to the left.

**Relationship:**

` Mean < Median < Mode `

**Examples:** Test scores on easy exams, age at retirement and gestational age at birth.

### 3\. Zero Skewness (Symmetrical Distribution)

Zero skewness shows a perfectly symmetrical distribution where the mean, median and mode are equal. In a symmetrical distribution, the data points are evenly distributed around the central point.

**Relationship:**

` Mean = Median = Mode `

**Example:** A perfectly balanced dataset with equal frequencies of all values.

## Tests of Skewness

There are several ways to find the skewness of a dataset:

### 1\. Visual Inspection

This is the simplest and quickest method for assessing skewness by creating a histogram or a density plot of the given data.

- If the plot has a long tail on the right, the data is positively skewed (right-skewed)
- If the plot has a long tail on the left, the data is negatively skewed (left-skewed)
- If the plot is roughly symmetric, the data has no skewness (zero skew)

### 2\. Skewness Coefficient (Pearson's First Coefficient of Skewness)

This is a numerical measure of skewness based on the relationship between the mean and mode.

**Formula:**

` Skewness = Mean − Mode `

- **Positive Skew:** If the mean is greater than the mode, the skewness is positive
- **Negative Skew:** If the mean is smaller than the mode, the skewness is negative
- **Zero Skew:** If the mean is equal to the mode, the skewness is zero

### 3\. Skewness Based on Quartiles

This method checks the distances between the quartiles to find skewness. If the quartiles are not equidistant, it suggests skewness.

The third quartile (Q3) minus the median (Me) should ideally be equal to the median (Me) minus the first quartile (Q1) in a symmetric distribution.

## Measurement of Skewness

### 1\. Karl Pearson's Measure

Karl Pearson's Measure uses the mean, median and standard deviation of the given data to measure the asymmetry of the distribution.

**Formulas:**

With respect to Mean and Median:

` Sk = 3 × (Mean − Median) / σ `

With respect to Mean and Mode:

` Sk = (Mean − Mode) / σ `

Where:

- Sk is Karl Pearson's skewness coefficient
- Mean = Mean of the dataset
- M = Median of the dataset
- σ = Standard deviation of the dataset

**Interpretation:**

- **Skewness = 0:** The distribution is symmetric
- **Skewness > 0:** The distribution is positively skewed (right-skewed)
- **Skewness < 0:** The distribution is negatively skewed (left-skewed)

### 2\. Bowley's Measure

Bowley's Skewness Coefficient is based on quartiles (Q1, Q2, Q3). Unlike Karl Pearson's measure it does not rely on the mean or standard deviation.

**Formula:**

` B = (Q3 + Q1 − 2Q2) / (Q3 − Q1) `

Where:

- Q1 = First quartile (25th percentile)
- Q2 = Second quartile (50th percentile or median)
- Q3 = Third quartile (75th percentile)

**Interpretation:**

- **B = 0:** The distribution is perfectly symmetric
- **B < 0:** The distribution is negatively skewed (left-skewed)
- **B > 0:** The distribution is positively skewed (right-skewed)

### 3\. Kelly's Measure

Kelly's Skewness Measure calculates skewness by comparing certain percentiles in the data, typically the 10th, 50th (median) and 90th percentiles.

**Formula:**

` SKL = (P90 + P10 − 2P50) / (P90 − P10) `

Where:

- P90 = 90th percentile
- P50 = 50th percentile (Median)
- P10 = 10th percentile

**Interpretation:**

- **SKL > 0:** Positive skew (right tail is longer)
- **SKL < 0:** Negative skew (left tail is longer)
- **SKL ≈ 0:** The distribution is symmetric

## Interpretation of Skewness

### Direction of Skewness

1.  **Negative Skewness (Left Skewed):**

    - The tail on the left side is longer
    - Most data points are concentrated on the right side
    - The mean is less than the median

2.  **Positive Skewness (Right Skewed):**

    - The tail on the right side is longer
    - Most data points are concentrated on the left side
    - The mean is greater than the median

3.  **Zero Skewness (Symmetric):**

    - Data is evenly distributed on both sides of the mean
    - No skewness present

### Magnitude of Skewness

- **Skewness close to 0 (between -0.5 and 0.5):** Approximately symmetric
- **Skewness below -1:** Strong left skewness
- **Skewness above 1:** Strong right skewness

## Handling Skewness in Data

### 1\. Data Transformation

- **Log Transformation:** Useful for right-skewed data
- **Square Root/Cube Root:** Helps reduce positive skew, especially for count data
- **Box-Cox Transformation:** A flexible method for handling both positive and negative skew

### 2\. Removing Outliers

- **Z-score:** Identify and remove data points with z-scores beyond ±3
- **IQR Method:** Remove data points beyond 1.5 times the interquartile range

### 3\. Non-Parametric Tests

When transformations aren't effective, consider:

- Mann-Whitney U Test
- Kruskal-Wallis Test

### 4\. Machine Learning Models

Some models handle skewed data better:

- **Tree-based Models:** Decision trees and random forests
- **Generalized Linear Models (GLM):** Use appropriate link functions

## Difference between Dispersion and Skewness

` Aspect Dispersion Skewness Definition Measures the spread of data around the central valueMeasures the shape of the distribution and directionMeasuresVariance, standard deviation, range, IQRPearson's coefficient, moment skewness, Q-Q plotsRelationship to MeanAffects the mean's interpretationShows the relationship between mean and medianInterpretationHigh dispersion = widely spread dataPositive/negative/zero skew indicates tail directionPurposeUnderstand variability of dataIdentify shape and asymmetry of dataExamplesTest scores spread, stock price variabilityIncome distribution, exam scores `

## Code Examples

This repository includes Jupyter notebooks demonstrating:

1.  **pearson_skewness.ipynb** - Karl Pearson's measure of skewness
2.  **bowley_skewness.ipynb** - Bowley's measure of skewness
3.  **kelly_skewness.ipynb** - Kelly's measure of skewness
4.  **visual_skewness.ipynb** - Visual inspection and plotting
5.  **handling_skewness.ipynb** - Data transformation techniques

## Getting Started

### Prerequisites

bash

` pip install numpy pandas matplotlib seaborn scipy `

### Running the Notebooks

1.  Clone this repository
2.  Install the required packages
3.  Open Jupyter Notebook or JupyterLab
4.  Navigate to the notebook files and run them

## Conclusion

By mastering the concept of skewness and understanding its measurement, we can easily assess data distributions, make informed decisions and apply the right techniques to our analyses.
