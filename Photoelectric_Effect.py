# Plotting stopping potential vs frequency of incident light
import numpy as np
import matplotlib.pyplot as plt
import scipy.stats as stats

# Given data: frequencies (in Hz) and corresponding stopping potentials (in V)
frequencies = np.array([4.72e14,5.26e14,5.56e14,6e14,6.38e14])  
stopping_potentials = np.array([0.46,0.61,0.78,0.91,1.18])  
stop_pot_err= np.array([0.05, 0.02, 0.03, 0.04, 0.06]) 

#Fitting with linear regression
slope, intercept, r_value, p_value, std_err = stats.linregress(frequencies, stopping_potentials)
print(f"Slope (h/e): {slope}")
print(f"Intercept (-W/e): {intercept}")

# Calculate Planck's constant and work function
e = 1.602e-19  # Charge of electron in Coulombs
h = slope * e  # Planck's constant
W = -intercept * e  # Work function
print(f"Calculated Planck's constant (h): {h} J·s")

# Plotting the data and the fitted line with error bars
plt.errorbar(frequencies, stopping_potentials, yerr=stop_pot_err, fmt='o', color='blue', label='Data Points with Error Bars')
plt.plot(frequencies, intercept + slope * frequencies, 'r', label='Fitted Line')
plt.xlabel('Frequency (Hz)')
plt.ylabel('Stopping Potential (V)')
plt.title('Photoelectric Effect: Stopping Potential vs Frequency')
plt.legend()
plt.grid()
plt.show()

#Calculating R-squared value
ss_res = np.sum((stopping_potentials - (intercept + slope * frequencies))**2)
ss_tot = np.sum((stopping_potentials - np.mean(stopping_potentials))**2)
r_squared = 1 - (ss_res / ss_tot)
print(f"R-squared: {r_squared}")

#Calculating work function in eV
W_eV = W / e
print(f"Work function (W): {W_eV} eV")
