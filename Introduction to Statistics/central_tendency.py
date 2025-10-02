import numpy as np
import scipy.stats as stats

# Measures of Central Tendency (Mean, Mode, Median)

# Sample Data
data_set_1 = [5, 6, 11, 4, 8, 10, 9]
data_set_2 = [1, 2, 2, 3, 4, 4, 4, 5, 5, 5]

# --- 1. Mean (Average) ---
mean = np.mean(data_set_1)
print(f"Dataset 1: {data_set_1}")
print(f"Mean = {mean:.4f}")

# --- 2. Mode (Most Frequent Value) ---
# Note: stats.mode returns a ModeResult object
mode_result = stats.mode(data_set_2, keepdims=False)
print(f"\nDataset 2: {data_set_2}")
print(f"Mode = {mode_result.mode} (Count: {mode_result.count})")

# --- 3. Median (Middle Value) ---
# For an even number of points, it's the average of the two middle values.
data_set_3 = [1, 2, 3, 4] 
median_val = np.median(data_set_3)
print(f"\nDataset 3: {data_set_3}")
print(f"Median = {median_val}")