# Thermal Conductivity by Lee's Method

## Aim of the Experiment
To determine the thermal conductivity of a bad conductor by measuring the rate of heat flow through the material under steady-state conditions using Lee's method

## Idea behind the Experiment

Heat transfer through solids occurs primarily via conduction. The quantitative description of this process is given by **Fourier’s Law of Heat Conduction**, which states that the rate of heat flow through a material is proportional to the temperature gradient across it. For a homogeneous slab of thickness ($l$) and cross-sectional area ($A$), the rate of heat transfer is:

$$\frac{dQ}{dt} = k \frac{A}{l}(T_2 - T_1)$$

where ($k$) is the thermal conductivity of the material, and ($T_2$), ($T_1$) are the temperatures of the two faces of the slab.

In Lee’s disc method, a poor conductor is sandwiched between two metallic discs. The upper disc is maintained at a higher temperature using steam, while heat flows through the specimen to the lower brass disc. After sufficient time, the system reaches a **steady state**, in which the temperature of each component becomes constant. Under this condition, the rate of heat conducted through the specimen equals the rate at which heat is lost by the lower disc to the surroundings.

The heat loss from the lower brass disc is governed by **Newton’s Law of Cooling**, which states that the rate of cooling of a body is proportional to the temperature difference between the body and its surroundings:

$$\frac{dT}{dt} = -b(T - T_a)$$

where ($T_a$) is the ambient temperature and ($b$) is a constant depending on the nature of the surface and surroundings.

If the brass disc has mass ($m$) and specific heat ($s$), the rate at which it loses heat is given by:

$$\frac{dQ}{dt} = ms \frac{dT}{dt}$$

At steady state, the heat conducted through the specimen equals the heat lost by the brass disc:

$$k \frac{A}{l}(T_2 - T_1) = ms \frac{dT}{dt}$$

Thus, the thermal conductivity ($k$) of the bad conductor is:

$$k = \frac{msl}{A(T_2 - T_1)} \left(\frac{dT}{dt}\right)$$

The cooling rate ($\frac{dT}{dt}$) is experimentally determined from the cooling curve of the brass disc obtained after removing the specimen. A representative slope value at the steady temperature is used for the calculation.

## Observations:
- Least count of the screw gauge = 0.01 mm
- Zero error of the screw gauge = -0.05 mm
- Zero correction = +0.05 mm
- Thickness of the glass disc = 3.79 mm
- Diameter of the glass disc = 11.1 cm
- Thickness of the ebonite disc = 3.25 mm
- Diameter of the ebonite disc = 11.15 cm

<div align="center">

| Time (s) | $T_{\text{ebonite}}$ (°C) | $T_{\text{glass}}$ (°C) |
|:--------:|:--------------:|:------------:|
| 0        | 88.7           | 88.0         |
| 15       | 88.0           | 86.5         |
| 30       | 85.9           | 83.0         |
| 45       | 83.8           | 80.0         |
| 60       | 81.8           | 77.3         |
| 75       | 80.1           | 74.8         |
| 90       | 78.8           | 73.8         |
| 105      | 77.6           | 72.9         |
| 120      | 76.6           | 72.1         |
| 135      | 75.6           | 71.5         |
| 150      | 74.9           | 70.9         |
| 165      | 74.1           | 70.4         |
| 180      | 73.5           | 69.9         |
| 195      | 72.9           | 69.5         |
| 210      | 72.4           | 69.1         |
| 225      | 71.8           | 68.8         |
| 240      | 71.2           | 68.5         |
| 255      | 70.8           | 68.2         |
| 270      | 70.3           | 67.9         |
| 285      | 69.7           | 67.6         |
| 300      | 69.2           | 67.3         |

</div>

## Plots
<div align="center">
<img width="701" height="547" alt="image" src="https://github.com/user-attachments/assets/4e72f194-5505-4c53-a6eb-116be82ecf7b" />

</div>


```python
import numpy as np
import matplotlib.pyplot as plt
import scipy.stats as stats
from scipy.optimize import curve_fit

# Given data
ebonite_thickness = 3.79 #mm
ebonite_diameter = 11.1 #cm
t = np.array([0, 15, 30, 45, 60, 75, 90, 105, 120, 135, 150, 165, 180, 195, 210, 225, 240, 255, 270, 285, 300])
T = np.array([88.7, 88, 85.9, 83.8, 81.8, 80.1, 78.8, 77.6, 76.6, 75.6, 74.9, 74.1, 73.5, 72.9, 72.4, 71.8, 71.2, 70.8, 70.3, 69.7, 69.2])

# Exponential Fit in accordance with Newton's cooling
def exp_fit(t, T_env, T0, k_cool):
    return T_env + (T0 - T_env) * np.exp(-k_cool * t)

popt, _ = curve_fit(exp_fit, t, T, p0=(30, T[0], 0.01))
T_exp = exp_fit(t, *popt)

# Linear Fit near steady state (~79.1°C)
mask = (T >= 78) & (T <= 81)

t_subset = t[mask]
T_subset = T[mask]

slope, intercept, *_ = stats.linregress(t_subset, T_subset)
T_linear = intercept + slope * t

# Plot 
plt.figure(figsize=(8,6))
plt.scatter(t, T, label='Data', color='blue')  # Data
plt.plot(t, T_exp, 'g--', label=f'Exp Fit (Cooling)')  # Exponential fit
plt.plot(t, T_linear, 'r', label=f'Local Linear Fit\nslope={slope:.4f} °C/s')  # Local linear fit (highlight region)
plt.scatter(t_subset, T_subset, color='black', zorder=3, label='Steady Region')  # Highlight subset points
plt.axhline(79.1, color='gray', linestyle=':', label='Steady Temp')
plt.xlabel('Time (s)')
plt.ylabel('Temperature (°C)')
plt.title("Cooling Curve with Exponential Fit and Local Linear Approximation for Ebonite")
plt.legend()
plt.grid()
plt.show()

print(f"Cooling constant (exp fit): {popt[2]:.5f} 1/s")
print(f"Slope near steady state: {slope:.5f} °C/s")

# Using the slope from the linear fit to calculate thermal conductivity
area_in_m2 = np.pi * (ebonite_diameter/2)**2 / 10000  # Convert cm^2 to m^2
thickness_in_m = ebonite_thickness / 1000  # Convert mm to m
k_linear = - (m * specific_heat_brass * slope * thickness_in_m) / (area_in_m2 * (T1 - T2))
print(f"Thermal conductivity from linear fit: {k_linear:.4f} W/m·K")
```
> Cooling constant (exp fit): 0.00667 1/s  
> Slope near steady state: -0.10000 °C/s  
> Thermal conductivity from linear fit: 0.4601 W/m·K  
> Estimated error in thermal conductivity: ±0.0354 W/m·K  
> Thermal conductivity of ebonite: 0.4601 ± 0.0354 W/m·K  
> R2 for linear fit: 0.9941089837997052  

<div align="center">
<img width="692" height="547" alt="image" src="https://github.com/user-attachments/assets/ab9c2a50-8965-427b-a4b1-899fa7ba14ea" />

</div>

```python
import numpy as np
import matplotlib.pyplot as plt
import scipy.stats as stats
from scipy.optimize import curve_fit

# Given data
glass_thickness = 3.79 #mm
glass_diameter = 11.1 #cm
t = np.array([0, 15, 30, 45, 60, 75, 90, 105, 120, 135, 150, 165, 180, 195, 210, 225, 240, 255, 270, 285, 300])
T = np.array([88, 86.5, 83, 80, 77.3, 74.8, 73.8, 72.9, 72.1, 71.5, 70.9, 70.4, 69.9, 69.5, 69.1, 68.8, 68.5, 68.2, 67.9, 67.6, 67.3])

# Exponential Fit in accordance with Newton's cooling-
def exp_fit(t, T_env, T0, k_cool):
    return T_env + (T0 - T_env) * np.exp(-k_cool * t)

popt, _ = curve_fit(exp_fit, t, T, p0=(30, T[0], 0.01))
T_exp = exp_fit(t, *popt)

# Linear Fit near steady state (~82.3°C)

t_subset = t[mask]
T_subset = T[mask]

slope, intercept, *_ = stats.linregress(t_subset, T_subset)
T_linear = intercept + slope * t

# Plot
plt.figure(figsize=(8,6))
plt.scatter(t, T, label='Data', color='blue')  # Data
plt.plot(t, T_exp, 'g--', label=f'Exp Fit (Cooling)')  # Exponential fit
plt.plot(t, T_linear, 'r', label=f'Local Linear Fit\nslope={slope:.4f} °C/s')  # Local linear fit (highlight region)
plt.scatter(t_subset, T_subset, color='black', zorder=3, label='Steady Region')  # Highlight subset points
plt.axhline(79.1, color='gray', linestyle=':', label='Steady Temp')
plt.xlabel('Time (s)')
plt.ylabel('Temperature (°C)')
plt.title("Cooling Curve with Exponential Fit and Local Linear Approximation for Glass")
plt.legend()
plt.grid()
plt.show()

print(f"Cooling constant (exp fit): {popt[2]:.5f} 1/s")
print(f"Slope near steady state: {slope:.5f} °C/s")

# Using the slope from the linear fit to calculate thermal conductivity
area_in_m2 = np.pi * (glass_diameter/2)**2 / 10000  # Convert cm^2 to m^2
thickness_in_m = glass_thickness / 1000  # Convert mm to m
k_linear = - (m * specific_heat_brass * slope * thickness_in_m) / (area_in_m2 * (T1 - T2))
print(f"Thermal conductivity from linear fit: {k_linear:.4f} W/m·K")
```

> Cooling constant (exp fit): 0.01237 1/s  
> Slope near steady state: -0.19000 °C/s  
> Thermal conductivity from linear fit: 1.4110 W/m·K  
> Estimated error in thermal conductivity: ±0.0429 W/m·K  
> Thermal conductivity of ebonite: 1.4110 ± 0.0429 W/m·K  
> R2 for linear fit: 0.9990774907749078  

