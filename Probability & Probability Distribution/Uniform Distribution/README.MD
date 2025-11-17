# Uniform Distribution: The Rectangular Distribution 🟦

The **Uniform Distribution**, also known as the **Rectangular Distribution**, is a **Continuous Probability Distribution** where all outcomes within a specified interval $[a, b]$ are **equally likely**. This results in a distinctive "flat" or constant probability density over the entire range.

---

## 1. Key Concepts

A uniform distribution models scenarios where there is **no systematic bias** toward any value in the given range.

- **Interval $[a, b]$:** Defines the range of possible values, where $a$ is the lower bound and $b$ is the upper bound.
- **Constant Density:** Unlike the Normal Distribution, where density peaks at the mean, the uniform distribution maintains the same probability density for every point within its interval.

### Probability Density Function (PDF)

The PDF is a constant value across the interval, and zero outside it:

$$f(x) = \begin{cases} \frac{1}{b-a} & \quad \text{for } a \le x \le b \\ 0 & \quad \text{for } x < a \text{ or } x > b \end{cases}$$

**Example:** For a uniform distribution on $[0, 25]$, the density is $f(x) = \frac{1}{25-0} = 0.04$.

### Cumulative Distribution Function (CDF)

The CDF gives the probability that the random variable $X$ is less than or equal to a specific value $x$. It is the linear accumulation of the density:

$$F(x) = \begin{cases} 0 & \quad \text{if } x < a \\ \frac{x-a}{b-a} & \quad \text{if } a \le x \le b \\ 1 & \quad \text{if } x > b \end{cases}$$

---

## 2. Properties

The properties of the uniform distribution are easily calculated from its bounds, $a$ and $b$.

| Property                  | Formula                              | Interpretation                         |
| :------------------------ | :----------------------------------- | :------------------------------------- |
| **Expected Value (Mean)** | $E[X] = \frac{a+b}{2}$               | The central point of the distribution. |
| **Variance**              | $Var(X) = \frac{(b-a)^2}{12}$        | Measures the spread around the mean.   |
| **Standard Deviation**    | $\sigma = \sqrt{\frac{(b-a)^2}{12}}$ | The measure of dispersion.             |

**Example Calculation (Using $a=0, b=25$):**

- **Mean:** $E[X] = \frac{0+25}{2} = 12.5$
- **Variance:** $Var(X) = \frac{(25-0)^2}{12} = \frac{625}{12} \approx 52.08$
- **Standard Deviation:** $\sigma \approx \mathbf{7.21}$

---

## 3. Applications in Data Science

The Uniform Distribution is vital for modeling pure randomness and for foundational tasks in data science:

- **Random Sampling/Simulation**: Used heavily in **Monte Carlo simulations** and machine learning training to generate truly random numbers (e.g., initial weight randomization in neural networks).
- **Quality Control**: Modeling variations in a production process when no particular measurement is favored.
- **Lottery and Gaming**: Generating random outcomes where selection fairness is required (e.g., shuffling algorithms, random number generators).
- **Time Modeling**: If an event (like a server request) is equally likely to occur at any time within a minute, the time of occurrence can be modeled uniformly.

---

## 4. Python Implementation

The accompanying file, `uniform_distribution_plot.py`, demonstrates how to generate and visualize samples from a uniform distribution, confirming its characteristic flat shape.

### `uniform_distribution_plot.ipynb`

```python
# uniform_distribution_plot.ipynb

import numpy as np
import matplotlib.pyplot as plt

# Define the interval [a, b]
a = 0
b = 25
num_samples = 1000

# 1. Generate random samples from the uniform distribution
samples = np.random.uniform(a, b, num_samples)

# 2. Plot the histogram of the samples
plt.hist(samples, bins=30, density=True, alpha=0.6, color='g')

# 3. Plot the theoretical PDF (the constant line)
x = np.linspace(a, b, 1000)
pdf_value = 1 / (b - a)
plt.plot(x, np.ones_like(x) * pdf_value, 'r-', lw=2, label=f'PDF = {pdf_value:.2f}')

plt.title('Uniform Distribution PDF (Histogram & Theoretical)')
plt.xlabel('X')
plt.ylabel('Probability Density')
plt.legend()
plt.show()
```
