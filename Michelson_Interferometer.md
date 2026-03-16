# Michelson's Interferometer

## Aim of the Experiment
To determine the refractive index of a transparent material (microscope glass slide) by measuring the Brewster angle.

## Theory

A coherent monochromatic light source (typically a laser) is incident on a **partially silvered beam splitter**, which divides the beam into two parts. One part is reflected toward mirror **M₁**, while the other is transmitted toward mirror **M₂**. After reflection from the mirrors, the beams return to the beam splitter, where they recombine and interfere. The resulting interference pattern of bright and dark fringes is observed on a screen or detector.

<p align="center">
  <img src="https://github.com/user-attachments/assets/488a27a1-7ee5-4744-863b-c3c8f7a9e102" width="700">
</p>

If the optical paths of the two beams differ by an integer multiple of the wavelength, **constructive interference** occurs and a bright fringe is observed. If the path difference equals an odd multiple of half the wavelength, **destructive interference** occurs, producing a dark fringe.

When one of the mirrors (usually M₁) is displaced by a small distance `d`, the optical path difference between the two beams changes by **twice the displacement**, because the beam travels the distance twice (forward and backward). As the mirror moves, the interference pattern shifts and fringes move across the field of view.

Each time the optical path difference changes by one wavelength, one fringe passes the reference point.

Thus, if `N` fringes pass when the mirror is displaced by distance `d`, the wavelength of the light is given by

$$\lambda = \frac{2d}{N}$$

If the displacement is measured using a micrometer screw gauge with calibration constant `δ`, the expression becomes

$$\lambda = \frac{2d}{N} \times \delta$$

where:

- `λ` = wavelength of the laser light  
- `d` = measured mirror displacement  
- `N` = number of fringes shifted 
- `δ` = micrometer calibration constant  

---

### Determination of the Refractive Index of Air

A sealed **air cell** of length `x` is placed in one arm of the interferometer. Initially the cell contains air at atmospheric pressure `P`. When the pressure inside the cell is changed by a small amount `ΔP`, the refractive index of air changes correspondingly.

Since the **optical path length** depends on the refractive index `n`, a change in `n` produces a change in the optical path difference between the two beams. As a result, the interference fringes shift.

The optical path length through a medium is given by

$$\text{Optical Path Length} = n \times d$$


When the refractive index changes, the optical path difference between the two interfering beams changes, causing `N` fringes to move across the field of view. From this fringe shift, the refractive index of air can be determined.

The relationship between the refractive index of air and the observed fringe shift is

$$N = \left(\frac{2d(n-1)}{\lambda}\right)\left(\frac{\Delta P}{P_0}\right)$$

where:

- `n` = refractive index of air  
- `d` = length of the air cell  
- `λ` = wavelength of the laser light  
- `$P0$` = atmospheric pressure  
- `ΔP` = change in pressure in the air cell

```python
# Michelson Interference
# Estimating the calibration constant
import numpy as np
import matplotlib.pyplot as plt
import scipy.stats as stats
displacements= np.array([0.18, 0.24, 0.29, 0.34, 0.41])  
fringe_counts = np.array([20, 25, 30, 35, 40])  
lambda_light = 532e-6  # Wavelength of light in mm (e.g., He-Ne laser)
# Calculate the calibration constant (k)

# plotting fringe counts vs displacements and fitting a line
slope, intercept, r_value, p_value, std_err = stats.linregress(displacements, fringe_counts)
print(f"Slope (k): {slope} fringes/mm")
print(f"Intercept: {intercept} fringes")
eq_label=rf"Fit: y={slope:.2f}*x + {intercept:.2f}"
plt.scatter(displacements, fringe_counts, color='blue', label='Data Points')
plt.plot(displacements, intercept + slope * displacements, 'r', label=eq_label)
plt.xlabel('Displacement, d (mm)')
plt.ylabel(r'Fringes Shifted ($\Delta N$)')
plt.title('Fringes Shifted vs Displacement plot')
plt.legend()
plt.grid()
plt.show()

# calculating r-squared value
ss_res = np.sum((fringe_counts - (intercept + slope * displacements))**2)
ss_tot = np.sum((fringe_counts - np.mean(fringe_counts))**2)
r_squared = 1 - (ss_res / ss_tot)
print(f"R-squared: {r_squared}")

# Calculating the calibration constant k
#lambda = 2 * displacement * k / fringe_counts
k = slope * lambda_light / 2
print(f"Calibration constant (k): {k} ")

# Calculating the wavelength of light using the calibration constant
new_displacement = np.array([0.25, 0.31, 0.38, 0.45, 0.5])
new_fringe_counts = np.array([20, 25, 30, 35, 40])

# plotting fringe counts vs displacements and fitting a line
slope, intercept, r_value, p_value, std_err = stats.linregress(new_displacement, new_fringe_counts)
print(f"Slope (k): {slope} fringes/mm")
print(f"Intercept: {intercept} fringes")
eq_label=rf"Fit: y={slope:.2f}*x + {intercept:.2f}"
plt.scatter(new_displacement, new_fringe_counts, color='blue', label='Data Points')
plt.plot(new_displacement, intercept + slope * new_displacement, 'r', label=eq_label)
plt.xlabel('Displacement, d (mm)')
plt.ylabel(r'Fringes Shifted ($\Delta N$)')
plt.title('Fringes Shifted vs Displacement plot')
plt.legend()
plt.grid()
plt.show()

# Calculating the wavelength of light using the new calibration constant 
lambda_calculated = 2*k/slope
print(f"Calculated wavelength of light: {lambda_calculated} mm")
# Wavelength in nm
lambda_calculated_nm = lambda_calculated * 1e6
print(f"Calculated wavelength of light: {lambda_calculated_nm} nm")

# r2 value for the second fit
ss_res = np.sum((new_fringe_counts - (intercept + slope * new_displacement))**2)
ss_tot = np.sum((new_fringe_counts - np.mean(new_fringe_counts))**2)
r_squared = 1 - (ss_res / ss_tot)
print(f"R-squared: {r_squared}")

# calculating the refractive index of air
fringe=np.array([5,10,15,20,25])
pressure=np.array([90,133,175,240,303])-41 #mmHg
atm_pressure=760 #mmHg

#plotting fringe counts vs pressure and fitting a line
slope, intercept, r_value, p_value, std_err = stats.linregress(pressure, fringe)
eq_label=rf"Fit: y={slope:.2f}*x + {intercept:.2f}"
plt.scatter(pressure, fringe, color='blue', label='Data Points')
plt.plot(pressure, intercept + slope * pressure, 'r', label=eq_label)
plt.xlabel(r'Pressure, $\Delta P$ (mmHg)')
plt.ylabel(r'Fringes Shifted, $\Delta N$')
plt.title('Fringes Shifted vs Pressure plot')
plt.legend()
plt.grid()
plt.show()
print(f"Slope: {slope} fringes/mmHg")
print(f"Intercept: {intercept} fringes")

#r2 value for the fit
ss_res = np.sum((fringe - (intercept + slope * pressure))**2)
ss_tot = np.sum((fringe - np.mean(fringe))**2)
r_squared = 1 - (ss_res / ss_tot)
print(f"R-squared: {r_squared}")

# calculating the refractive index of air
d= 10 #cm Length of pressure chamber
n_air = 1 + (slope * atm_pressure * lambda_light) / (2 * d * 1e7)
print(f"Refractive index of air: {n_air} ")
```
