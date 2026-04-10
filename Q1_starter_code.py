import numpy as np
import scipy.interpolate as int
import matplotlib.pyplot as plt

# Data
xs = np.array([-1.50, 0.500, 1.20, 3.10, 4.60])
ys = np.array([-0.400, 1.60, 6.60, 11.0, 12.03])

# Cubic spline
S = int.CubicSpline(xs, ys)

# Plot range
xPlot = np.linspace(min(xs)-0.5, max(xs)+0.5, 200)

# Function values
yPlot = S(xPlot)

# First derivative
dSdx = S.derivative(1)
yPlot2 = dSdx(xPlot)

# Second derivative
dSdxdx = S.derivative(2)
yPlot3 = dSdxdx(xPlot)

# Third derivative
dSdxdxdx = S.derivative(3)
yPlot4 = dSdxdxdx(xPlot)

# Plot everything
plt.plot(xPlot, yPlot, label='Spline')
plt.plot(xPlot, yPlot2, label='1st derivative')
plt.plot(xPlot, yPlot3, label='2nd derivative')
plt.plot(xPlot, yPlot4, label='3rd derivative')
plt.plot(xs, ys, 'o', label='Data')

plt.legend()
plt.xlabel('x')
plt.ylabel('y')
plt.title('Cubic spline interpolant and its derivatives')

# SAVE IMAGE (IMPORTANT for LaTeX)
plt.savefig("spline_plot.png")
plt.show()