# Bayes' Theorem: Updating Probabilities with Evidence 🧠

**Bayes' Theorem** is a fundamental mathematical formula used to determine the **conditional probability** of a hypothesis, known as the **Posterior Probability**, by incorporating **prior knowledge** and **new evidence**. It is the engine behind Bayesian Inference, allowing probabilities to be revised as new data emerges.

---

## 1. The Core Formula

Bayes' Theorem reverses the conditioning in a conditional probability statement. It allows us to find $P(\text{Hypothesis } \mid \text{Evidence})$ when we know $P(\text{Evidence} \mid \text{Hypothesis})$.

For two events A and B, the formula is:

$$P(A \mid B) = \frac{P(B \mid A) \times P(A)}{P(B)}$$

Where:
* $\mathbf{P(A \mid B)}$: **Posterior Probability** (What we want: Probability of A given B).
* $\mathbf{P(B \mid A)}$: **Likelihood** (Probability of B given A).
* $\mathbf{P(A)}$: **Prior Probability** (Initial probability of A).
* $\mathbf{P(B)}$: **Marginal Probability** (Probability of B occurring, calculated using the Law of Total Probability).

---

## 2. The Law of Total Probability (The Denominator)

When there are multiple mutually exclusive and exhaustive hypotheses ($E_1, E_2, \dots, E_n$), the probability of the evidence ($P(A)$) is calculated by summing the joint probabilities of the evidence occurring under each hypothesis. This forms the denominator of the generalized Bayes' formula.

$$\mathbf{P(A)} = \sum_{k=1}^{n} P(E_k) \cdot P(A \mid E_k)$$

### Generalized Bayes' Theorem

$$P(E_i \mid A) = \frac{P(E_i) \cdot P(A \mid E_i)}{\sum_{k=1}^{n} P(E_k) \cdot P(A \mid E_k)}$$

---

## 3. Key Terminology

| Term | Notation | Description |
| :--- | :--- | :--- |
| **Hypotheses** | $E_1, E_2, \dots$ | Possible causes or events (e.g., having a disease). |
| **Prior Probability**| $P(E_i)$ | Initial probability *before* evidence is considered. |
| **Likelihood** | $P(A \mid E_i)$ | Probability of the evidence (A) *given* the hypothesis ($E_i$) is true. |
| **Posterior Probability**| $P(E_i \mid A)$ | **Updated** probability of the hypothesis *after* observing the evidence (A). |

---

## 4. Applications

Bayes' Theorem is crucial in fields requiring probabilistic reasoning and belief updating:
* **AI & Machine Learning**: Used in **Naïve Bayes classifiers** for tasks like text classification and spam filtering.
* **Medical Diagnostics**: Calculating the actual probability of having a disease after a positive test result, accounting for false positives/negatives.
* **Risk Management**: Updating financial models based on new market data.

---

## 5. Difference from Conditional Probability

While Bayes' Theorem is derived from conditional probability, its purpose is distinct:

| Feature | Conditional Probability ($P(A \mid B)$) | Bayes' Theorem ($P(A \mid B)$) |
| :--- | :--- | :--- |
| **Purpose** | Finds the direct probability of A given B. | Finds the **reverse** probability, often to update a hypothesis (Prior $\rightarrow$ Posterior). |
| **Calculation** | Uses $P(A \cap B)$ and $P(B)$. | Uses $P(B \mid A)$, $P(A)$, and $P(B)$ (via Total Probability). |

---

## 6. Python Practice Problems

The accompanying file, `bayes_problems.py`, solves the practice questions using the concepts of conditional probability, joint probability, and Bayes' Theorem.