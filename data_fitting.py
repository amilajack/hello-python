import numpy as np
from scipy import optimize
import matplotlib.pyplot as plt

x = np.array([
  -3.14159265358979,
  -2.81089869005402,
  -2.48020472651826,
  -2.14951076298249,
  -1.81881679944672,
  -1.48812283591095,
  -1.15742887237519,
  -0.82673490883942,
  -0.49604094530365,
  -0.16534698176788,
  0.16534698176788,
  0.49604094530365,
  0.82673490883942,
  1.15742887237519,
  1.48812283591095,
  1.81881679944672,
  2.14951076298249,
  2.48020472651826,
  2.81089869005402,
  3.14159265358979
])

y = np.array([
  0.00000000000000,
  -0.43702230525987,
  -0.78170987707147,
  -0.85207605602719,
  -0.52335935447908,
  0.22121102681686,
  1.27130734031775,
  2.41089249371528,
  3.37539264122665,
  3.92749194128624,
  3.92749194128624,
  3.37539264122665,
  2.41089249371528,
  1.27130734031775,
  0.22121102681686,
  -0.52335935447908,
  -0.85207605602719,
  -0.78170987707147,
  -0.43702230525987,
  0.0000000000000,
])

# Plot the data points
plt.plot(x,y, label='Data')

# Plot polynomial fit
polyfit = np.poly1d(np.polyfit(x, y, 4))
plt.plot(x,polyfit(x), label='4th Degree Polynomial')


def trig_poly_fit(x, a0, a1, a2, a3, b1, b2):
    return a0/2+(a3/2)*np.cos(3*x)+a1*np.cos(x)+a2*np.cos(2*x)+b1*np.sin(x)+b2*np.sin(2*x)

# Plot trigonometric fit
params, params_covariance = optimize.curve_fit(trig_poly_fit, x, y)
plt.plot(x, trig_poly_fit(x, *params), label='Trigonometric Polynomial')

plt.legend(loc='best')
plt.show()
