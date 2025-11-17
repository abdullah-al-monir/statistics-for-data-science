# Exponential Distribution: Modeling Time Until an Event ⏳

The **Exponential Distribution** is a continuous probability distribution widely used to model the **time** or **space** elapsed between events in a **Poisson process**. Essentially, it describes the waiting time until the next random event occurs, assuming the rate of occurrence is constant.

---

## 1. Core Functions

The Exponential Distribution is defined by a single parameter: the **rate parameter** $\mathbf{\lambda}$ (lambda), which represents the average frequency of events (e.g., calls per minute).

### A. Probability Density Function (PDF)

The PDF calculates the likelihood of the waiting time being exactly $x$:

$$f(x; \lambda) = \lambda e^{-\lambda x}, \quad x \ge 0$$

### B. Cumulative Distribution Function (CDF)

The CDF gives the probability that the event occurs **within time $x$** ($X \le x$):

$$F(x; \lambda) = 1 - e^{-\lambda x}, \quad x \ge 0$$

---

## 2. Key Properties

### Mean and Variance

The mean and variance are directly determined by the rate parameter $\lambda$.

| Measure                       | Formula                        | Interpretation                            |
| :---------------------------- | :----------------------------- | :---------------------------------------- |
| **Mean (Expected Wait Time)** | $E[X] = \frac{1}{\lambda}$     | The average time between events.          |
| **Variance**                  | $Var(X) = \frac{1}{\lambda^2}$ | Measures the spread of the waiting times. |

### Memoryless Property

The exponential distribution is the only continuous distribution with the **memoryless property**: the probability of waiting longer does **not** depend on how long you have already waited.

$$P(X > s + t \mid X > s) = P(X > t)$$

---

## 3. Example: Customer Support Calls

**Problem**: Calls arrive at a support center at an average rate of **$\lambda = 2$ per minute**. What is the probability that you wait **more than 30 seconds** for the next call?

1.  **Define Rate and Time Units**:

    - Rate: $\lambda = 2$ calls per minute.
    - Time: Convert 30 seconds to $x = 0.5$ minutes.

2.  **Calculate $P(X > x)$**: We use the complement of the CDF, $P(X > x) = 1 - F(x; \lambda)$, which simplifies to $e^{-\lambda x}$.

$$P(X > 0.5) = e^{-(2 \cdot 0.5)} = e^{-1} \approx \mathbf{0.3679}$$

There is a **36.79%** chance the next call will arrive _after_ 30 seconds.

---

## 4. Real-World Applications

The exponential distribution is closely linked to the **Poisson distribution** (which models the _number_ of events in a fixed time).

- **Service Systems**: Modeling time between customer arrivals in queues (banks, web servers, call centers).
- **Reliability Engineering**: Modeling the time until a product or machine part fails.
- **Transport**: Analyzing the time between buses, trains, or traffic events.

---

## 5. Python Implementation

The accompanying file, `exponential_distribution_plot.py`, generates and visualizes data following an exponential distribution. Note that NumPy uses the **scale parameter** ($\beta$) which is $\mathbf{1/\lambda}$.

### `exponential_distribution_plot.ipynb`

```python
# exponential_distribution_plot.ipynb

import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Set the rate parameter lambda (events per unit time)
lam = 1.5

# Calculate the scale parameter (beta) for numpy
# scale = 1/lambda
scale = 1 / lam

# Generate exponential data (1000 samples)
data = np.random.exponential(scale=scale, size=1000)

# Plot the Kernel Density Estimate (KDE) and histogram
sns.histplot(data, kde=True, stat="density")
plt.title(f"Exponential Distribution (λ={lam})")
plt.xlabel("Time (x)")
plt.ylabel("Density")
plt.show()
```
