import math
from math import sin, cos, pi
from numpy import arange, array, vectorize
from pylab import plot, show
from matplotlib.animation import FuncAnimation, PillowWriter
from matplotlib.patches import ConnectionPatch
import matplotlib.pyplot as plt

g = 9.81
l = 0.1
frame_rate = 30


def calculate_points(theta_1=pi / 6, theta_2=pi / 3):
    a = 0.0
    b = 10.0
    N = 10000
    h = (b - a) / N

    tpoints = arange(a, b, h)
    t1, t2, w1, w2 = [], [], [], []
    r = array([theta_1, theta_2, 0., 0.], float)
    for t in tpoints:
        t1.append(r[0])
        t2.append(r[1])
        w1.append(r[2])
        w2.append(r[3])

        k1 = h * f(r, t)
        k2 = h * f(r + 0.5 * k1, t + 0.5 * h)
        k3 = h * f(r + 0.5 * k2, t + 0.5 * h)
        k4 = h * f(r + k3, t + h)
        r += (k1 + 2 * k2 + 2 * k3 + k4) / 6

    return t1, t2


def anim(t1, t2):
    b1x, b1y = [], []
    b2x, b2y = [], []

    steps = arange(0, len(t1), 1000 / frame_rate, dtype=int)

    for theta_1, theta_2 in zip(t1, t2):
        b1x.append(l * sin(theta_1))
        b1y.append(-l * cos(theta_1))
        b2x.append(l * (sin(theta_1) + sin(theta_2)))
        b2y.append(-l * (cos(theta_1) + cos(theta_2)))

    fig = plt.figure()
    ax = plt.axes(xlim=(-2.2 * l, 2.2 * l), ylim=(-2.2 * l, 0))
    ax.set_axis_off()
    arc1, = plt.plot([], [], lw=1, color='orange')
    arc2, = plt.plot([], [], lw=1, color='orange')

    def init():
        bob_patch_1 = plt.Circle((b1x[0], b1y[0]), 0.01)
        bob_patch_2 = plt.Circle((b2x[0], b2y[0]), 0.01)

        pendulum_1 = ConnectionPatch((0, 0), (b1x[0], b1y[0]), coordsA="data")
        pendulum_2 = ConnectionPatch((b1x[0], b1y[0]), (b2x[0], b2y[0]), coordsA="data")

        ax.add_patch(bob_patch_2)
        ax.add_patch(bob_patch_1)
        ax.add_patch(pendulum_1)
        ax.add_patch(pendulum_2)

        arc1.set_data([],[])
        arc2.set_data([],[])

        return bob_patch_1, bob_patch_2, pendulum_2, pendulum_1, arc1, arc2

    def animate(i):
        n = steps[i]
        ax.patches = []
        bob_patch_1 = plt.Circle((b1x[n], b1y[n]), 0.01)
        bob_patch_2 = plt.Circle((b2x[n], b2y[n]), 0.01)

        pendulum_1 = ConnectionPatch((0, 0), (b1x[n], b1y[n]), coordsA="data")
        pendulum_2 = ConnectionPatch((b1x[n], b1y[n]), (b2x[n], b2y[n]), coordsA="data")

        ax.add_patch(bob_patch_2)
        ax.add_patch(bob_patch_1)
        ax.add_patch(pendulum_1)
        ax.add_patch(pendulum_2)

        arc1.set_data(b1x[max(0, n-500):n], b1y[max(0, n-500):n])
        arc2.set_data(b2x[max(0, n-500):n], b2y[max(0, n-500):n])

        return bob_patch_1, bob_patch_2, pendulum_2, pendulum_1, arc1, arc2

    a = FuncAnimation(fig, animate, init_func=init, frames=len(steps),
                                interval=int(1000 / frame_rate), blit=True, repeat=False)

    # a.save("double_pendulum_85_85.gif", writer=PillowWriter(fps=15))
    plt.show()


def f(r, t):
    theta_1 = r[0]
    theta_2 = r[1]
    omega_1 = r[2]
    omega_2 = r[3]

    ftheta_1 = omega_1
    ftheta_2 = omega_2

    fomega_1 = -(omega_2 ** 2 * sin(2 * theta_1 - 2 * theta_2) + 2 * omega_2 ** 2 * sin(theta_1 - theta_2) + (g / l) * (
            sin(theta_1 - 2 * theta_2) + 3 * sin(theta_1))) / (3 - cos(2 * theta_1 - 2 * theta_2))
    fomega_2 = (4 * omega_1 ** 2 * sin(theta_1 - theta_2) + omega_2 ** 2 * sin(2 * theta_1 - 2 * theta_2) + 2 * (
            g / l) * (sin(2 * theta_1 - theta_2) - sin(theta_2))) / (3 - cos(2 * theta_1 - 2 * theta_2))
    return array([ftheta_1, ftheta_2, fomega_1, fomega_2], float)


if __name__ == "__main__":
    t1, t2 = calculate_points(theta_1=84 * pi / 180., theta_2=84 * pi / 180.)
    anim(t1, t2)
