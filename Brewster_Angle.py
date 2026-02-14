# Determination of refractive index using brewster's angle
import numpy as np
import matplotlib.pyplot as plt

inc_angles = np.array([10,15,20,25,30,35,40,45,50,55,60,65,70,])  
current1 = np.array([42, 40.1, 39.5, 46.4, 47.7, 35.8, 23.2, 11.6, 5.5, 0.4, 1.6, 19.4, 40.8,])
current2= np.array([67.1, 71.2, 69.8, 65.6, 44.8, 39.1, 22.4, 13.4, 4.6, 0.4, 1.8, 20, 66.1])
current3 = np.array([91, 96, 58.6, 52.8, 39.3, 37.6, 24.7, 12.3, 4.4, 0.5, 2.4, 17.4, 54.2])
current4= np.array([69.4, 100, 90, 63, 47.7, 43.2, 29.8, 11.7, 5.2, 1.1, 2.7, 23.8, 162])
current5= np.array([70.2, 90.1, 80.5, 60.4, 45.8, 40.3, 25.6, 10.9, 4.8, 0.6, 1.9, 18.7, 50.3])
current= (current1+current2+current3+current4+current5)/5
stddev= np.std([current1,current2,current3], axis=0, ddof=1)


#plotting current vs incident angle with error bars
plt.errorbar(inc_angles, current, yerr=stddev, fmt='o-.', color='blue', label='Average Current with Std Dev')
plt.xlabel('Incident Angle (degrees)')
plt.ylabel('Current (µA)')
plt.title('Current vs Incident Angle with Error Bars')
plt.legend()
plt.grid()
