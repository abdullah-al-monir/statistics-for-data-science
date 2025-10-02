import numpy as np
import statistics

# Measures of Variability (Range, Variance, Standard Deviation)

# Sample Data
arr = [1, 2, 3, 4, 5]
print(f"Sample Data: {arr}")

# --- 1. Range (Max - Min) ---
maximum = max(arr)
minimum = min(arr)
data_range = maximum - minimum
print(f"\nMaximum = {maximum}, Minimum = {minimum}")
print(f"Range = {data_range}")

# --- 2. Variance (Average squared deviation from the mean) ---
# statistics.variance() calculates the sample variance (divides by n-1)
variance_val = statistics.variance(arr)
print(f"\nSample Variance (Var) = {variance_val:.1f}")

# --- 3. Standard Deviation (Square root of the Variance) ---
# statistics.stdev() calculates the sample standard deviation
std_dev_val = statistics.stdev(arr)
print(f"Sample Standard Deviation (Std) = {std_dev_val:.4f}")

# Note: numpy.var() and numpy.std() calculate population variance/std by default (divides by n).
# To get sample variance, you must use ddof=1 (Delta Degrees of Freedom)
numpy_sample_variance = np.var(arr, ddof=1)
print(f"NumPy Sample Variance (np.var(ddof=1)) = {numpy_sample_variance:.1f}")