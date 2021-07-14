import matplotlib.pyplot as plt
import numpy as np


def basic_rocket_body(center=np.array([0, 0]), scale=1, angle=0):

    points = np.array([[-.30, -.20],
                       [-.30, .20],
                       [.30, .20],
                       [.50, .0],
                       [.30, -.20]])*scale
    rotation = [[np.cos(angle), -np.sin(angle)], [np.sin(angle), np.cos(angle)]]
    for i in range(len(points)):
        np.matmul(rotation, points[i], out=points[i])
    points = points + center

    return plt.Polygon(points, color='red')
