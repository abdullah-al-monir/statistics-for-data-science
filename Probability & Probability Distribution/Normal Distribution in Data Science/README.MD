# Normal (Gaussian) Distribution in Data Science 🔔

The **Normal Distribution**, also known as the **Gaussian Distribution** or **Bell Curve**, is the most widely used probability distribution in statistics. Its symmetry and predictable characteristics make it fundamental to inferential statistics, especially the **Central Limit Theorem (CLT)**.

---

## 1. Core Characteristics

The Normal Distribution is characterized by its parameters:

- $\mathbf{\mu}$ **(Mu)**: The **mean**, which defines the center of the distribution.
- $\mathbf{\sigma}$ **(Sigma)**: The **standard deviation**, which measures the spread or dispersion of the data.

### Probability Density Function (PDF)

The function that defines the bell-shaped curve is:

$$f_X(x) = \frac{1}{\sigma\sqrt{2\pi}} e^{-\frac{1}{2}(\frac{x-\mu}{\sigma})^2}$$

The term $\mathbf{z = \frac{x-\mu}{\sigma}}$ is the **z-score**, which measures how many standard deviations a data point ($x$) is from the mean.

### The Empirical Rule (68-95-99.7)

For any normally distributed dataset, the probability of an event occurring is concentrated around the mean:

- **68%** of the data falls within $\mathbf{\pm 1\sigma}$ of the mean.
- **95%** of the data falls within $\mathbf{\pm 2\sigma}$ of the mean.
- **99.7%** of the data falls within $\mathbf{\pm 3\sigma}$ of the mean.

---

## 2. Standard Normal Distribution

The **Standard Normal Distribution** is a special case where:

- **Mean** ($\mu$) is set to **0**.
- **Standard Deviation** ($\sigma$) is set to **1**.

All normal distributions can be converted into the Standard Normal Distribution using the z-score formula. This standardization is crucial because it allows the use of a single, standardized table (the Z-table) to find cumulative probabilities for _any_ normal distribution.

### Cumulative Distribution Function (CDF)

The CDF, denoted $\mathbf{P(Z \le z)}$, gives the cumulative probability of a random variable being less than or equal to a specific value ($x$ or $z$). Since the Normal CDF lacks a simple closed-form formula, it is typically calculated via the **Z-table** after standardizing the data.

## 3. Expectations and Variability

- **Expected Value** ($\mathbf{E[X]}$): For a normal distribution, the expected value is simply the **mean**, $\mathbf{\mu}$.
  $$E[X] = \mu$$

- **Variance** ($\mathbf{\sigma^2}$): Measures the average squared deviation from the mean.
- **Standard Deviation** ($\mathbf{\sigma}$): The square root of the variance, used as the primary measure of spread.

---

## 4. Example: Finding Probability via Z-Score

**Problem**: Current measurements ($X$) are Normal with $\mu = 10$ and $\sigma^2 = 4$ ($\sigma = 2$). Find $P(X > 13)$.

1.  **Standardize (Find Z-score):**
    $$Z = \frac{X - \mu}{\sigma} = \frac{13 - 10}{2} = 1.5$$

2.  **Find Cumulative Probability:**
    Using the Z-table, $P(Z \le 1.5) = 0.93319$

3.  **Calculate Final Probability:**
    $$P(X > 13) = P(Z > 1.5) = 1 - P(Z \le 1.5) = 1 - 0.93319 = \mathbf{0.06681}$$
    The probability is approximately $\mathbf{6.7\%}$.

---

## 5. Applications in Various Fields

The Normal Distribution models many real-world phenomena:

- **Scientific Research**: Modeling measurement errors in experiments.
- **Finance**: Assessing risk and volatility, as stock returns often follow a normal distribution.
- **Engineering**: Modeling manufacturing tolerances and quality control.
- **Healthcare/Psychometrics**: Describing biological measurements (e.g., blood pressure) and standardized test scores (e.g., IQ).

---

## 6. Python Implementation

The accompanying file, `normal_distribution_plot.py`, demonstrates how to generate and visualize a normal distribution using Python libraries.

### `normal_distribution_plot.ipynb`

```python

import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Define parameters for the distribution
mean = 10
std_dev = 2
size = 1000

# Generate normally distributed random data
data = np.random.normal(loc=mean, scale=std_dev, size=size)

# Create a histogram with a Kernel Density Estimate (KDE) line
sns.histplot(data, kde=True, stat="density", bins=30, color="skyblue", linewidth=0.8)

# Add titles and labels
plt.title(f'Normal Distribution (μ={mean}, σ={std_dev})')
plt.xlabel('Value')
plt.ylabel('Density')
plt.show()
```
