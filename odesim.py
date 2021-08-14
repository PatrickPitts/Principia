from math import sin, pi
from numpy import array, arange
from pylab import plot, xlabel, show

g = 9.81
l = 0.1


def f(r, t):
    theta = r[0]
    omega = r[1]
    ftheta = omega
    fomega = -g / l * sin(theta)
    return array([ftheta, fomega], float)


a = 0.0
b = 100.0
N = 1000
h = (b - a) / N

tpoints = arange(a, b, h)
theta_points = []
omega_points = []

r = array([179. * pi / 180., 0.], float)

for t in tpoints:
    theta_points.append(r[0])
    omega_points.append(r[1])
    k1 = h * f(r, t)
    k2 = h * f(r + 0.5 * k1, t + 0.5 * h)
    k3 = h * f(r + 0.5 * k2, t + 0.5 * h)
    k4 = h * f(r + k3, t + h)
    r += (k1 + 2 * k2 + 2 * k3 + k4) / 6

print(theta_points)
#
# plot(tpoints, theta_points)
# plot(tpoints, omega_points)
# xlabel("t")
# show()
