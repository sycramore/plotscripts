import numpy as np
import matplotlib.pyplot as plt
import scipy.optimize as opt
import copy

# -----------------------------
# Load spectrum data
# -----------------------------
# Tab-separated file with four columns: energy, imax, itotal, ibackground
energy, imax, itotal, ibackground = np.loadtxt(
    'examplespectrum.dat', usecols=(0, 2, 3, 4), unpack=True
)

# Subtract background
imax_clean = np.array(imax) - np.array(ibackground)
itotal_clean = np.array(itotal) - np.array(ibackground)

print("Energy values:", energy)

# -----------------------------
# Define Lorentzian model
# -----------------------------
def lorentzian(x, s, t):
    # s = FWHM, t = center of the peak
    return (1 / np.pi) * (s / (s**2 + (x - t) ** 2))

# -----------------------------
# Fit data (adjust interval!)
# -----------------------------
fit_start, fit_end = 122, 139
x_fit = energy[fit_start:fit_end]
y_fit = imax_clean[fit_start:fit_end]

fit_params, covariance = opt.curve_fit(lorentzian, x_fit, y_fit)

print("Fit parameters [FWHM, center]:", fit_params)
print("Covariance matrix:\n", covariance)
print("Peak center located at:", fit_params[1], "eV")

# -----------------------------
# Plot full spectrum and fitted peak
# -----------------------------
plt.plot(energy, imax_clean, label='Background-corrected data')
plt.plot(x_fit, lorentzian(x_fit, *fit_params), 'r--', label='Lorentzian fit')
plt.title('Maximal intensity vs. energy – I(V) curve')
plt.xlabel('Energy (eV)')
plt.ylabel('Intensity')
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.savefig("spectrum_fit.png", dpi=300)
plt.show()

# -----------------------------
# Helper: Find index range for a given energy interval
# -----------------------------
energy_list = list(energy)
first_energy = 386  # adjust this!
last_energy = 437   # adjust this!

try:
    i_start = energy_list.index(first_energy)
    i_end = energy_list.index(last_energy)
    print("Data index range for selected interval:", i_start, "to", i_end)
except ValueError:
    print("One of the selected energy values is not in the dataset.")

