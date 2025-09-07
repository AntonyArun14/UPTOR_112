import numpy as np

# data = np.linspace(0, 10, 100)
# print(data)

# data = [np.random.normal(0, 1, 100), np.random.normal(0, 1.5, 100), np.random.normal(0, 2, 100)]
# print(data)
# print(len(data))

# """Using IQR method (Inter Quaratile Method)"""
# import matplotlib.pyplot as plt
# import pandas as pd
#
# np.random.seed(42)
#
# data = np.random.normal(50, 5, 100) # Mean 50, Standard Deviation 5, 100 Scale (No of Datas)
#
# data = np.append(data, [80, 85, 90])  # Add outliers
#
# df = pd.DataFrame(data, columns=["value"])
#
#
# Q1 = df["value"].quantile(0.25)
# Q3 = df["value"].quantile(0.75)
# IQR = Q3 - Q1
#
# # Outlier definition
# lower = Q1 - 1.5 * IQR
# upper = Q3 + 1.5 * IQR
# outliers_iqr = df[(df["value"] < lower) | (df["value"] > upper)]
#
# print("Detected Outliers (IQR):")
# print(outliers_iqr)
# #
# # Plot
# plt.figure(figsize=(10,5))
# plt.boxplot(df["value"], vert=False)
# plt.axvline(lower, color="r", linestyle="--")
# plt.axvline(upper, color="r", linestyle="--")
# plt.title("Outlier Detection using IQR")
# plt.show()

"""below code is again for the same but using different methods"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import zscore

# Sample data (normally distributed with some outliers)
np.random.seed(42)
data = np.random.normal(50, 5, 100)
data = np.append(data, [80, 85, 90,])  # Add outliers

df = pd.DataFrame(data, columns=["value"])

# Z-Score method
z_scores = np.abs(zscore(df["value"]))
threshold = 3
outliers = df[z_scores > threshold]

print("Detected Outliers (Z-Score):")
print(outliers)

# Plot
plt.figure(figsize=(10,5))
plt.boxplot(df["value"], vert=False)
plt.title("Outlier Detection using Z-Score (Boxplot)")
plt.show()
