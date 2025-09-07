import numpy as np
import matplotlib.pyplot as plt

# ==============================
# 1. Standard Normal Distribution (mean=0, std=1)
# ==============================
standard_normal = np.random.randn(1000)  # draws from N(0,1)

# ==============================
# 2. Normal Distribution (mean=50, std=10)
# ==============================
normal = np.random.normal(loc=50, scale=10, size=1000)  # N(50,10)

# ==============================
# 3. Plot both
# ==============================
plt.figure(figsize=(10, 5))

# Plot Standard Normal
plt.hist(standard_normal, bins=30, alpha=0.6, color='blue', label="Standard Normal (mean=0, std=1)", density=True)

# Plot Normal
plt.hist(normal, bins=30, alpha=0.6, color='orange', label="Normal (mean=50, std=10)", density=True)

plt.legend()
plt.title("Standard Normal vs Normal Distribution")
plt.xlabel("Value")
plt.ylabel("Density")
plt.show()
