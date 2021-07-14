import numpy as np
import matplotlib.pyplot as plt
from Mathematics import cartesian2d_to_polar2d, polar2d_to_cartesian2d


class ProjectileMotion2d:
    def __init__(self, x0=0, y0=0, vx=None, vy=None, theta=None, v=None, g=-9.81):
        self.x0 = x0
        self.y0 = y0
        self.g = g
        if vx is None and vy is None and v is not None and theta is not None:
            self.theta = theta
            self.v = v
            self.vx, self.vy = polar2d_to_cartesian2d(v, theta)
        elif vx is not None and vy is not None and v is None and theta is None:
            self.vx = vx
            self.vy = vy
            self.v, self.theta = cartesian2d_to_polar2d(vx, vy)
        else:
            raise ValueError("Projectile Motion: Bad Parameters: cannot infer mechanics from provided parameters")

    def __str__(self):
        return "r(0) = ({x0}, {y0})\nv = {v}, theta = {theta}\n" \
               "vx = {vx}, vy = {vy}\ng = {g}".format(x0=self.x0, y0=self.y0, v=self.v, theta=self.theta, vx=self.vx,
                                                      vy=self.vy, g=self.g)

    def range(self):
        t = (-self.vy - np.sqrt(self.vy ** 2 - 2 * self.g * self.y0)) / self.g
        return self.vx * t + self.x0, t

    def vectorized_positions(self, t0=0, tf=1, n_steps=10):
        pos = np.vectorize(lambda t: (self.x0 + self.vx * t,
                                      self.y0 + self.vy * t + 0.5 * self.g * t ** 2,
                                      np.arctan((self.vy + self.g * t) / self.vx)))
        return pos(np.linspace(t0, tf, n_steps, endpoint=True))

    def max_height(self):
        return -self.vy ** 2 / (2 * self.g)


def projectile_max_height(x0=0, y0=0, vx=None, vy=None, theta=None, v=None, g=-9.81):
    if vx is not None and vy is not None:
        pass
    elif vx is None and vy is None and v is not None and theta is not None:
        vy = np.sin(theta) * v
        vx = np.cos(theta) * v
    else:
        print("Bad parameters")

    return -vy ** 2 / (2 * g)


def projectile_range(x0=0, y0=0, vx=None, vy=None, theta=None, v=None, g=-9.81):
    if vx is not None and vy is not None:
        pass
    elif vx is None and vy is None and v is not None and theta is not None:
        vy = np.sin(theta) * v
        vx = np.cos(theta) * v
    else:
        print("Bad parameters")

    t = max(np.polynomial.polynomial.Polynomial((y0, vy, 0.5 * g)).roots())
    if t < 0:
        raise ValueError("Projectile Range: Bad Parameters: Results in negative range")
    return vx * t + x0, t


def projectile_motion_2d_vectorized(x0=0, y0=0, vx=None, vy=None, theta=None, v=None, g=-9.81, t1=0, t2=1, n_steps=10):
    pos = None
    if theta is None and v is None:
        pos = np.vectorize(lambda t: (x0 + vx * t, y0 + vy * t + 0.5 * g * t * t))
    elif vx is None and vy is None:
        pos = np.vectorize(lambda t: (x0 + np.cos(theta) * v * t, y0 + np.sin(theta) * v * t + 0.5 * g * t * t))
    else:
        print("Bad parameters")

    return pos(np.arange(t1, t2, (t2 - t1) / n_steps))

# t_range = 5 * np.sqrt(2) / (9.81 / 2)
#
# x, y = projectile_motion_2d_vectorized(v=10, theta=np.pi / 4, t2=t_range, n_steps=101)
# plt.plot(x, y, color='red')
# plt.show()
