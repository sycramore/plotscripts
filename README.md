# plotscripts

Simple scripts for plotting and fitting data in the natural sciences  
**Designed for students of chemistry, biology, medicine, and related fields**  
who don't want to deal with Igor, Origin – or simply can't afford Windows.

---

## Purpose

These scripts are built to help students quickly visualize and analyze their lab data.  
They focus on **basic polynomial fitting** – nothing fancy, just enough to get clean plots and reproducible fits for:

- first-year chemistry or physics labs  
- reports and presentations  
- basic regression tasks in introductory science courses

They are intentionally kept simple, to avoid distractions and reduce friction when plotting.

---

## Why this?

Because sometimes you just want to:

- **Fit a curve** without worrying about how `polyfit()` works  
- **Plot your data** without clicking through five menus  
- **Avoid commercial software** that runs only on expensive hardware or Windows  
- **Get your lab report done** without fighting GUIs or licensing hell

If you're taking chemistry as a minor, or doing just a few physics or biostats labs – this might be all you need.

---

## Educational context

Many of us had to:

- draw plots by hand using graph paper and rulers in our **first semester**
- implement a linear least squares fit **from scratch** in the **second semester**
- use **Mathematica** (once) – then never again  
- resort to **Gnuplot**, R, or whatever script worked on Linux

These scripts continue that spirit: lightweight, minimal, and focused.

---

## Features

- Polynomial least squares fits (default: linear)
- Output of fit parameters and covariance matrix
- Automatic plot generation and export (`fit_plot.png`)
- Easy to adapt for:
  - **Logarithmic transformations** (e.g. linearizing exponentials)
  - **Parabolic fits** (e.g. when doing Taylor expansions near a minimum)
  - **Subsets of data** (just slice your array)

---

## Dependencies

```yaml
dependencies:
  - numpy
  - scipy
  - matplotlib

