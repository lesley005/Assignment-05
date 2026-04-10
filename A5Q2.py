# Lesley Ozurigbo
# 100904794

import numpy as np
import matplotlib.pyplot as plt
from LS import *

# Data from question 2:
xs = np.array([-1.00, 0.200, 2.40, 3.60, 4.70])
ys = np.array([-1.400, 0.60, 2.60, 4.1, 5.15])

# Linear least squares (order 1)
P, a = LS(xs, ys, 1)

# Plot
xPlot = np.linspace(min(xs)-0.5, max(xs)+0.5, 100)
yPlot = np.array([P(x) for x in xPlot])

plt.plot(xs, ys, 'o', label='Data')
plt.plot(xPlot, yPlot, '-', label='Least squares line')
plt.xlabel('x')
plt.ylabel('y')
plt.legend()
plt.show()

# Compute least squares error
err = 0.0
for i in range(5):
    err += (ys[i] - P(xs[i]))**2

print('Least squares error is %e.' % (err))