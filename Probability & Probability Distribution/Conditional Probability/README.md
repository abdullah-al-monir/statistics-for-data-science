# Conditional Probability: The Power of 'Given' 🎲

**Conditional Probability** defines the likelihood of an event occurring **given that another event has already occurred**. It is fundamental to modeling dependent events and forms the basis for advanced statistical techniques like **Bayes' Theorem**.

---

## Core Concept and Formula

Conditional probability is denoted as $\mathbf{P(A \mid B)}$, which reads "the probability of **Event A** occurring, **given** that **Event B** has already occurred."

The formula is:

$$P(A \mid B) = \frac{P(A \cap B)}{P(B)}$$

Where:
* $\mathbf{P(A \cap B)}$ is the **Joint Probability**: the probability of **both** A and B occurring simultaneously.
* $\mathbf{P(B)}$ is the **Marginal Probability**: the probability of event B occurring.

---

## Key Concepts and Properties

### 1. Independent vs. Dependent Events

| Feature | Independent Events (e.g., Coin Tosses) | Dependent Events (e.g., Drawing Cards without Replacement) |
| :--- | :--- | :--- |
| **Relationship**| The outcome of one event **does not** affect the other. | The outcome of one event **affects** the probability of the other. |
| **Conditional Rule**| $P(A \mid B) = P(A)$ | $P(A \mid B) \neq P(A)$ |
| **Multiplication Rule**| $P(A \cap B) = P(A) \times P(B)$ | $P(A \cap B) = P(A) \times P(B \mid A)$ |

### 2. Properties

* **Sure Event**: $P(S \mid A) = P(A \mid A) = 1$
* **Complement Rule**: $P(A' \mid B ) = 1 - P( A \mid B )$
* **Non-Commutative**: In general, $P(A \mid B) \neq P(B \mid A)$.

### 3. Joint vs. Marginal Probability

| Parameter | Conditional ($P(A \mid B)$) | Joint ($P(A \cap B)$) | Marginal ($P(A)$) |
| :--- | :--- | :--- | :--- |
| **Definition** | Probability of A, given B has occurred. | Probability of A AND B occurring. | Probability of A occurring alone. |

---

## Applications

Conditional probability is the backbone for:
* **Finance & Risk Management**: Assessing default risk given financial indicators.
* **Healthcare & Diagnostics**: Determining disease probability given test results.
* **Machine Learning**: Classification, recommendation systems, and predicting user behavior.
* **Weather Forecasting**: Estimating future weather given current conditions.

---

## Python Implementation and Examples

The following files demonstrate the application of conditional probability, including solutions to the provided 'unsolved' questions:

| File | Topic | Description |
| :--- | :--- | :--- |
| `card_draw_example.py` | Dependent Events | Solves card drawing problems using the multiplication and conditional rules. |
| `survey_proportion.py` | Set Theory (Proportions) | Solves survey-based problems using the formula $P(A \mid B) = \frac{n(A \cap B)}{n(B)}$. |
| `bayes_and_total_prob.py` | Bayes' Theorem Application | Solves problems requiring the Law of Total Probability and Bayes' Theorem. |