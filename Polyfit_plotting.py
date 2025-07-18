import numpy as np
import matplotlib.pyplot as plt

# -----------------------------
# Load data from text file
# -----------------------------
data1, data2, data3 = np.loadtxt('exampledata.txt', usecols=(0, 1, 2), unpack=True)

# -----------------------------
# Polynomial least squares fit
# -----------------------------
deg = 1
fitparameter, covariance = np.polyfit(data1, data2, deg, full=False, cov=True)

print("Fit parameters:", fitparameter)
print("Covariance matrix:\n", covariance)

# -----------------------------
# Generate fit curve
# -----------------------------
fit = np.polyval(fitparameter, data1)

# -----------------------------
# Plot data and fit
# -----------------------------
plt.plot(data1, data2, 'ro', label='Data')
plt.plot(data1, fit, 'b-', label=f'Fit (deg={deg})')
plt.xlabel('data1')
plt.ylabel('data2')
plt.legend()
plt.grid(True)
plt.tight_layout()

# Save plot before showing
plt.savefig("fit_plot.png", dpi=300)
plt.show()

