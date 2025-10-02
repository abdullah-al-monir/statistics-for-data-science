# Introduction to Statistics: The Foundation of Data Science & Analytics 📊

Statistics provides the essential tools to collect, process, understand, and derive actionable insights from raw data, forming the backbone of modern data science and analytics.

---

## 1. Basic Statistical Terminology

| Term | Definition |
| :--- | :--- |
| **Data** | Facts, numbers, or observations collected for analysis. |
| **Variable** | A characteristic or attribute being measured (Quantitative or Qualitative). |
| **Population** | The complete set of individuals or data points of interest. |
| **Sample** | A subset of the population selected for analysis. |
| **Parameter** | A numerical description of a **Population** (often unknown). |
| **Statistic** | A numerical description of a **Sample** (used to estimate parameters). |

---

## 2. Types of Statistics

### 2.1. Descriptive Statistics
Summarize and describe the main features of a dataset. They provide simple summaries of the sample.

* **Measures of Central Tendency**: Mean, Median, Mode.
* **Measures of Variability (Dispersion)**: Range, Variance, Standard Deviation.

### 2.2. Inferential Statistics
Allow us to make predictions or inferences about a larger **Population** based on **Sample** data.

* **Techniques**: Confidence Intervals, Hypothesis Testing, Regression.

---

## 3. Types of Data & Levels of Measurement

### 3.1. Quantitative Data (Numerical)
Consists of numerical values that can be measured.
| Type | Description | Examples |
| :--- | :--- | :--- |
| **Discrete** | Countable values; cannot be divided (e.g., number of students). |
| **Continuous**| Measurable values; can take any value within a range (e.g., height, temperature). |

### 3.2. Qualitative Data (Categorical)
Describes qualities or characteristics; non-numerical.
| Type | Description | Examples |
| :--- | :--- | :--- |
| **Nominal** | Categories without order or ranking (e.g., gender, color). |
| **Ordinal** | Categories with a meaningful order or ranking (e.g., satisfaction ratings). |

### 3.3. Levels of Measurement (Analysis Feasibility)
| Level | Order | True Zero | Operations | Example |
| :--- | :--- | :--- | :--- | :--- |
| **Nominal**| No | No | Frequency counts, Mode | Types of fruit |
| **Ordinal** | Yes | No | Median, Mode | Education levels |
| **Interval**| Yes | No | Addition, Subtraction | Temperature, IQ scores |
| **Ratio** | Yes | Yes | All (+, -, ×, ÷) | Height, Weight, Income |

---

## 4. Descriptive Statistics in Detail

### 4.1. Measures of Central Tendency
Describe the center point of the data.

| Measure | Formula (Mean) | Python File |
| :--- | :--- | :--- |
| **Mean** | $\bar{x} = \frac{\sum x}{n}$ | `central_tendency.py` |
| **Mode** | Most frequently occurring value. | `central_tendency.py` |
| **Median** | The middle value in a sorted dataset. | `central_tendency.py` |

### 4.2. Measures of Variability (Dispersion)
Describe how spread out the data is.

| Measure | Formula (Variance) | Python File |
| :--- | :--- | :--- |
| **Range** | Max Value - Min Value | `variability.py` |
| **Variance**| $\sigma^2 = \frac{\sum(x-\mu)^2}{N}$ | `variability.py` |
| **Standard Deviation**| $\sigma = \sqrt{\frac{\sum(x-\mu)^2}{N}}$ | `variability.py` |

---

## 5. Inferential Statistics: Making Inferences

Inferential statistics allows us to generalize sample findings to the population.

| Technique | Description | Key Formula |
| :--- | :--- | :--- |
| **Confidence Intervals** | A range of values likely to contain the true population parameter. | $CI = \bar{x} \pm Z_{\alpha/2} \times \frac{\sigma}{\sqrt{n}}$ |
| **Hypothesis Testing**| Formal procedure to test claims (H₀ vs. H₁). Decided by comparing test statistic or **p-value** to a significance level ($\alpha$).| $Z = \frac{\bar{x} - \mu_0}{\sigma/\sqrt{n}}$ |
| **Central Limit Theorem (CLT)**| States sample means approximate a normal distribution as sample size ($n$) increases, crucial for parametric tests. | $\bar{X} \sim N(\mu, \frac{\sigma}{\sqrt{n}})$ |

### Errors in Testing
* **Type I Error ($\alpha$):** Wrongly **rejecting** a true Null Hypothesis (H₀).
* **Type II Error ($\beta$):** Wrongly **failing to reject** a false Null Hypothesis (H₀).

### Parametric vs. Non-Parametric Tests
* **Parametric**: Assumes data follows a specific distribution (e.g., Z-test, T-test).
* **Non-Parametric**: Makes no distributional assumptions (e.g., Chi-Square test).

---

## 6. Covariance and Correlation: Measuring Relationships

These measures quantify the relationship between two variables.

### 6.1. Covariance
Measures how two variables change together, indicating the **direction** of the linear relationship.
* **Range**: $(-\infty, +\infty)$
* **Positive Covariance**: Both variables increase/decrease together.
* **Negative Covariance**: One increases as the other decreases.
* **Formula (Sample)**: $Cov_S(X,Y) = \frac{1}{n-1}\sum_{i=1}^{n}(X_i-\bar{X})(Y_i-\bar{Y})$

### 6.2. Correlation (Pearson's $\rho$)
A standardized measure derived from covariance, indicating both the **direction and strength** of the linear relationship.
* **Range**: $[-1, +1]$
* **Close to +1**: Strong positive relationship.
* **Close to -1**: Strong negative relationship.
* **Close to 0**: No linear relationship.

| Feature | Covariance | Correlation |
| :--- | :--- | :--- |
| **Scale Dependence**| Dependent on variable units (has dimensions). | Independent of variable units (dimensionless). |
| **Primary Output** | Direction of relationship. | Direction **and strength** of relationship. |

---

## Python Implementation Examples

See the following files for Python code demonstrating basic descriptive statistics using `numpy` and `scipy`.