from numpy import sin, cos, pi, arange, array, zeros, vectorize, trapz
from matplotlib.pyplot import figure, plot, show

def main():

    # lower/upper bound
    A,B,N= 0.0, 1.0, 1000

    # number of partial sums used in the transform
    n_coefficients = 5

    # core function. CHANGE THIS.
    def f(x):
        return x**2
    # simulates f(x)*sin(2pi nx)
    def f_sin(n, x):
        return f(x)*sin(2*pi*n*x)
    def f_cos(n, x)
        return f(x)*cos(2*pi*n*x)

    x_val = arange(A, B, (B-A)/N, dtype=float)
    a_n, b_n = [], []
    for i in range(1, n_coefficients + 1):
        vfunc_a = vectorize(f_sin)
        vfunc_b = vectorize(f_cos)
        a_n.append(trapz(vfunc_a(i, x_val), dx = (B-A)/N)
        b_n.append(trapz(vfunc_b(i, x_val), dx = (B-A)/N)

    # generate sine coefficients
    # generate cosine coefficients
    # generate b_0




#     A, B, N = 0., 1.0, 1000
#
#     num_coefficients = 500
#
#     # generalized, current problem doesn't call for cosine coefficients
#     sin_coef = generate_sine_coefficients(num_coefficients)
#     cos_coef = generate_cosine_coefficients(num_coefficients)
#     def transform(val):
#         y = 1./3.
#         for i in range(len(sin_coef)):
#             a, b = sin_coef[i], cos_coef[i]
#             y += a * sin(i*val) + b * cos(i*val)
#         return y
#     x = arange(A, B, (B-A)/N, dtype=float)
#     f = vectorize(transform)
#     y = f(x)

    plot(x, y)
    plot(x, x**2)
    show()



def generate_sine_coefficients(coef):
    a = [i for i in range(1, coef+1)]
    f = vectorize(lambda n : -1.0/(n * pi * 2))
    return f(a)

def generate_cosine_coefficients(coef):
    a = [i for i in range(1, coef + 1)]
    f = vectorize(lambda n : 1.0/(2 * pi**2 * n**2))
    return f(a)

if __name__ == "__main__":
    main()