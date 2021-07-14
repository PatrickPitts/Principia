import numpy as np
import random
from fractions import Fraction


def quad_roots(a, b, c):
    d = b ** 2 - 4 * a * c
    return None


def cartesian2d_to_polar2d(x, y):
    return np.sqrt(x ** 2 + y ** 2), np.arctan(y / x) if x > 0 else np.arctan(y / x) + np.pi


def polar2d_to_cartesian2d(r, o):
    return r * np.cos(o), r * np.sin(o)


def generate_coefficient_matrix(**kwargs):
    max_rand = 10
    min_rand = -max_rand
    n_coefficients = 2

    # for i in range(4):
    #     #slopes, intercepts, coefficient
    #     mat = [[random.randint(min_rand, max_rand) for n in range(2)] for n in range(3)]
    for i in range(4):
        mat = [[random.randint(min_rand, max_rand) for n in range(n_coefficients)] for n in range(n_coefficients)]
        eq = [[random.randint(min_rand, max_rand)] for n in range(n_coefficients)]
        det = np.linalg.det(mat)
        if det == 0:
            print("Determinant is zero, no solutions to system")
            continue
        x_soln = mat[1][1] * eq[0][0] - mat[0][1] * eq[1][0]
        y_soln = mat[0][0] * eq[1][0] - mat[1][0] * eq[0][0]

        print('%sx + %sy = %s' % tuple(mat[0] + eq[0]))
        print('%sx + %sy = %s' % tuple(mat[1] + eq[1]))
        print('x = %s, y = %s' % tuple([str(Fraction(x_soln / det).limit_denominator()),
                                        str(Fraction(y_soln / det).limit_denominator())]))
        print()
