import numpy as np


def cartesian2d_to_polar2d(x, y):
    return np.sqrt(x ** 2 + y ** 2), np.arctan(y / x) if x > 0 else np.arctan(y / x) + np.pi


def polar2d_to_cartesian2d(r, o):
    return r * np.cos(o), r * np.sin(o)


def rad_to_deg(rad):
    return rad * 180. / np.pi


def deg_to_rad(deg):
    return deg * np.pi / 180.
