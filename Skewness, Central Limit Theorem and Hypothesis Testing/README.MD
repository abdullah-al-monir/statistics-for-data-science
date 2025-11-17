Use of Skewness, Central Limit Theorem and Hypothesis Testing in Data Science

In data science, we often work with samples instead of entire populations. The Central Limit Theorem (CLT) helps us assume normality in sample means, while Hypothesis Testing helps us make decisions based on those samples. These concepts are essential for tasks like A/B testing, model evaluation, and user behavior analysis.

## Skewness in Data Science

Skewness tells us whether the data is symmetric or tilted to one side. Understanding skewness is important before applying statistical methods that assume normality.

### Example: Income Distribution

Suppose a company's employee salaries are: \[25k, 28k, 30k, 32k, 35k, 36k, 100k\]

Most salaries are around 25k–36k, but one outlier (100k) pulls the average to the right.

> This is a positively skewed distribution. The mean will be higher than the median due to the high-income outlier.

## Central Limit Theorem (CLT) in Data Science

The Central Limit Theorem says that if we take many large samples and find their averages, those averages form a normal distribution even if the original data is skewed. This allows data scientists to use normal distribution formulas to calculate confidence intervals and error margins, even when the raw data is not normal.

### Example: Estimating Average Daily Orders

A delivery company wants to estimate the average daily orders without checking the full month’s data.

- Data (10 days): \[100, 200, ..., 700\], Population Mean = 360
- Sample Means: 262.5, 412.5, 425
- Avg. of Sample Means = 366.7 (close to 360)

This shows how the Central Limit Theorem helps small samples give a reliable estimate of the overall mean.

### Use cases

- Estimate delivery time from few days
- Analyze average spending from user samples
- Approximate server time without full logs

## Hypothesis Testing in Data Science

Hypothesis testing checks if a sample result is statistically different from a known or expected value. It helps in deciding whether to reject the null hypothesis based on a threshold called the significance level (commonly 0.05).

### Example: Has the Complaint Rate Decreased?

A company claims its new packaging reduced complaints. Earlier, 10% of orders had complaints. In a recent sample of 1000 orders, only 70 complaints were reported.

- H₀: Complaint rate = 10%
- H₁: Complaint rate < 10%
- Sample rate = 0.07
- z ≈ –3.16, Critical z = –1.645

Since –3.16 < –1.645, we reject H₀ there’s strong evidence the complaint rate has dropped.

### Applications

- Test if a website change improves clicks
- Compare two ML models
- Check if discounts increase sales
- Evaluate impact of process updates
