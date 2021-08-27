from numpy import array, vectorize, arange
from matplotlib.pyplot import figure, plot, show


def main():
    a, b, n = 1, 10, 1000
    t_step = (b-a)/n

    c_1 = 1.
    r_1 = 1.
    r_2 = 1.
    V_0 = 1.

    A_0 = 0.



    def rk():
        a, b, n = 0., 1., 10000
        h = (b-a)/n
        tpoints = arange(a, b, h)
        A, A_dot = [], []
        r = array([0., 0.], float)
        for t in tpoints:
            A.append(r[0])
            A_dot.append(r[1])

            k1 = h * f(r, t)
            k2 = h * f(r + 0.5 * k1, t + 0.5 * h)
            k3 = h * f(r + 0.5 * k2, t + 0.5 * h)
            k4 = h * f(r + k3, t + h)
            r += (k1 + 2 * k2 + 2 * k3 + k4) / 6
        return A

    def f(r, t):
        A = r[0]
        A_dot = r[1]

        fA = A_dot
        fA_dot = c_1*r_1 - (r_2)*fA/((r_1-r_2)*t + V_0)
        return array([fA, fA_dot], float)

    fig = figure()
    pts = rk()
    plot(arange(len(pts)), pts)
    show()
    return None

if __name__ == "__main__":
    main()