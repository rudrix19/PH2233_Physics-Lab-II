# Plotting 1/lambda vs (1/ni^2-1/nf^2)
lmbd=np.array([667.8362569, 468.6054375, 423.6281911, 383.6314041])
L=1/lmbd
X=np.array([0.138888889, 0.1875, 0.21, 0.222222222])
n=np.array([3,4,5,6])

#Fitting with linear regression
slope, intercept, r_value, p_value, std_err = stats.linregress(X, L)
print(f"Slope (R): {slope}")
print(f"Intercept (R): {intercept}")

eq_label=rf"Fit: y={slope:.5f}*x + {intercept:.5f}$"
plt.scatter(X,L)
plt.plot(X, intercept + slope * X, 'r', label=eq_label)
plt.xlabel('$n_i$')
plt.ylabel(r'$\frac{1}{{\lambda}}$')
plt.xticks(X, n)
plt.title("Determination of Rydberg's constant")
plt.legend()
plt.grid()
plt.show()

#Calculating R-squared value
ss_res = np.sum((L - (intercept + slope * X))**2)
ss_tot = np.sum((L - np.mean(L))**2)
r_squared = 1 - (ss_res / ss_tot)
print(f"R-squared: {r_squared}")
