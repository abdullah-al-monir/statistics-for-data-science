# Binomial Distribution: Modeling Success in Binary Trials 🎯

The **Binomial Distribution** is a discrete probability distribution that calculates the probability of a specific number of **successes** in a **fixed number ($n$) of independent trials**, where each trial has only two possible outcomes: **success** or **failure**.

It is widely used in quality control, election forecasting, medical testing, and customer behavior modeling.

---

## 1. Key Concepts

A scenario must meet four criteria to follow a Binomial Distribution:

1.  **Fixed Number of Trials ($n$):** The experiment is repeated a set number of times. (e.g., flipping a coin 5 times).
2.  **Bernoulli Trial:** Each trial results in only two outcomes: **Success** or **Failure**.
3.  **Independent Trials:** The outcome of one trial does not affect the outcome of any other trial.
4.  **Constant Probability:** The probability of success ($p$) remains the same for every trial.

| Parameter               | Notation | Description                                            |
| :---------------------- | :------- | :----------------------------------------------------- |
| **Number of Trials**    | $n$      | The fixed count of repetitions.                        |
| **Success Probability** | $p$      | The probability of success in a single trial.          |
| **Failure Probability** | $q$      | Calculated as $q = 1 - p$.                             |
| **Number of Successes** | $x$      | The specific number of successes we are interested in. |

---

## 2. Binomial Distribution Formulae

### A. Probability Mass Function (PMF)

The PMF calculates the probability of getting **exactly $x$ successes** in $n$ trials:

$$P(X=x) = \binom{n}{x} p^x (1-p)^{n-x}$$

Where $\binom{n}{x}$ is the **binomial coefficient**, representing the number of ways to arrange $x$ successes in $n$ trials:
$$\binom{n}{x} = \frac{n!}{x!(n-x)!}$$

### B. Cumulative Distribution Function (CDF)

The CDF gives the probability of getting **at most $x$ successes** ($x$ or fewer):

$$F(x) = P(X \le x) = \sum_{k=0}^{x} P(X=k)$$

---

## 3. Measures of Central Tendency and Spread

| Measure                   | Formula                                 | Interpretation                                                  |
| :------------------------ | :-------------------------------------- | :-------------------------------------------------------------- |
| **Expected Value (Mean)** | $E[X] = n \cdot p$                      | The average number of successes expected over many repetitions. |
| **Variance**              | $Var[X] = n \cdot p \cdot (1-p)$        | Measures the spread of the number of successes around the mean. |
| **Standard Deviation**    | $\sigma = \sqrt{n \cdot p \cdot (1-p)}$ | The typical deviation of the number of successes from the mean. |

---

## 4. Practical Example: Airline Overbooking

An airline sells $n=65$ tickets for a 60-seat flight. The probability a passenger shows up is $p=0.9$. To find the probability that **60 or fewer passengers show up** ($P(X \le 60)$), we use the complement rule:

$$P(X \le 60) = 1 - P(X > 60) = 1 - \sum_{x=61}^{65} P(X=x)$$

The result, after calculation, is:
$$P(X \le 60) \approx \mathbf{0.7909}$$

---

## 5. Applications in Data Science

- **Quality Control**: Modeling the number of defective items in a sample batch.
- **Medical Testing**: Predicting the number of positive results in a set of fixed, independent tests.
- **Customer Behavior**: Modeling the probability that a fixed number of customers will click an ad or purchase a product.

---

## 6. Python Implementation

The accompanying file, `binomial_distribution_plot.ipynb`, demonstrates how to calculate and visualize the PMF and CDF using the `scipy.stats` library.
