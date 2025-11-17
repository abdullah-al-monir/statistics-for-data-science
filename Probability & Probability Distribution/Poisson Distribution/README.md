# Poisson Distribution: Modeling Rare Events Over Time

The **Poisson Distribution** is a **discrete probability distribution** that models the probability of a specific number of independent events occurring in a **fixed interval** of time or space, given a **constant average rate** of occurrence. It's ideal for modeling rare, independent events like accidents, phone calls, or website hits.

---

## 1. Key Concepts

The Poisson Distribution is defined by a single parameter: $\mathbf{\lambda}$ (lambda).

- **Average Rate ($\mathbf{\lambda}$):** The mean number of occurrences expected in the fixed interval. This value is constant and central to the distribution.
- **Independence:** The occurrence of one event must not affect the probability of another event occurring.
- **Fixed Interval:** The observations must be confined to a specific, defined time period (e.g., one hour, one day) or spatial area (e.g., one square mile).

### Probability Mass Function (PMF)

The PMF calculates the probability of observing **exactly $x$ events** in the fixed interval:

$$P(X=x) = \frac{e^{-\lambda} \lambda^x}{x!}$$

Where:

- $e$: Euler's number ($\approx 2.718$).
- $\lambda$: The average rate of occurrence (mean).
- $x$: The number of events for which we calculate the probability ($x = 0, 1, 2, \dots$).

---

## 2. Measures and Functions

### Expected Value and Variance

A unique characteristic of the Poisson Distribution is that its mean, variance, and standard deviation are all derived directly from $\lambda$:

| Measure                   | Formula                   | Interpretation                                 |
| :------------------------ | :------------------------ | :--------------------------------------------- |
| **Expected Value (Mean)** | $E[X] = \lambda$          | The expected number of events in the interval. |
| **Variance**              | $Var[X] = \lambda$        | The spread of events around the mean.          |
| **Standard Deviation**    | $\sigma = \sqrt{\lambda}$ | The measure of dispersion.                     |

### Cumulative Distribution Function (CDF)

The CDF gives the probability of observing **at most $x$ events** ($X \le x$):

$$F(x) = P(X \le x) = \sum_{k=0}^{x} P(X=k)$$

---

## 3. Example: Call Center Analysis

**Problem**: A call center receives an average of $\mathbf{\lambda = 3}$ calls per hour. What is the probability of receiving **exactly 4 calls** ($x=4$) in one hour?

$$P(X=4) = \frac{e^{-3} 3^4}{4!} = \frac{e^{-3} \cdot 81}{24} \approx \mathbf{0.168}$$

The probability of receiving exactly 4 calls is approximately **16.8%**.

---

## 4. Relationship to Exponential Distribution

The Poisson and Exponential distributions model the two sides of the same phenomenon, known as the **Poisson process**:

- **Poisson Distribution (Discrete):** Models the **number of events** ($X=k$) in a fixed interval.
- **Exponential Distribution (Continuous):** Models the **waiting time** ($T=t$) between consecutive events.

Both are defined by the same rate parameter, $\lambda$ (the average rate of events per unit time/space).

---

## 5. Applications in Data Science

- **Traffic Analysis**: Modeling the number of vehicles or accidents at an intersection in a fixed duration.
- **Telecommunications**: Predicting the number of simultaneous network requests or server failures.
- **Queuing Theory**: Analyzing the arrival rate of customers at a service point (e.g., checkout line or bank).
- **Healthcare**: Modeling the occurrence of rare diseases or hospital admissions.

---

## 6. Python Implementation

The accompanying file, `poisson_distribution_plot.py`, demonstrates how to calculate and visualize the PMF and CDF using the `scipy.stats.poisson` library.

### `poisson_distribution_plot.ipynb`

```python

import matplotlib.pyplot as plt
import numpy as np
from scipy.stats import poisson

# Set the average rate (lambda)
lambda_val = 3
# Range of events to plot
k = np.arange(0, 10)

# 1. Probability Mass Function (PMF)
pmf = poisson.pmf(k, lambda_val)

plt.figure(figsize=(8, 6))
plt.bar(k, pmf, color='lightgreen', edgecolor='black')
plt.title(f'Poisson Distribution PMF (λ={lambda_val})')
plt.xlabel('Number of events (k)')
plt.ylabel('Probability')
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.show()

# 2. Cumulative Distribution Function (CDF)
cdf = poisson.cdf(k, lambda_val)

plt.figure(figsize=(8, 6))
plt.plot(k, cdf, color='purple', marker='o', linestyle='-', linewidth=2)
plt.title(f'Poisson Distribution CDF (λ={lambda_val})')
plt.xlabel('Number of events (k)')
plt.ylabel('Cumulative Probability')
plt.grid(True)
plt.show()

# Example calculation: Probability of exactly 4 events
probability_4_events = poisson.pmf(4, lambda_val)
print(f'Probability of exactly 4 events: {probability_4_events:.4f}')
# Output: Probability of exactly 4 events: 0.1680
```
