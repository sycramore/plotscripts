---

## Nonlinear Fit Example (Lorentzian Peak Fit)

The second script in this repo demonstrates how to perform **nonlinear least squares fits** using custom model functions – in this case, a **Lorentzian peak**, which is commonly used in spectroscopy.

### Use case

This script is useful for analyzing spectra that exhibit clear peaks, such as:

- Raman spectra  
- Infrared (IR) spectroscopy  
- Photoemission or LEED data  
- Any lab measurement where you want to extract **peak position** and **width**

The script subtracts a background signal, defines a Lorentzian model, and fits it to a selected interval of the spectrum. It also includes a **helper function to identify index ranges** for peak intervals based on energy values.

Even though the original dataset is no longer available, the script itself remains a clean, functional example of nonlinear fitting in Python.

### File included

| File              | Description                             |
|-------------------|-----------------------------------------|
| `peakfinder.py` | Performs Lorentzian fits to spectral peaks |
| `examplespectrum.dat` | (Missing) Example data file in tab-separated format |

> Feel free to generate your own test data or contact the author if you want to reconstruct a sample dataset.
