from numpy import empty, zeros, max
from pylab import imshow, gray, show
import datetime

def main():
    M = 100
    V = 1.00
    target = 1e-6

    phi=zeros([M+1, M+1], float)
    phi[0,:]=V
    phiprime=empty([M+1, M+1], float)

    delta = 1.0
#     for i in range(M+1):
#         for j in range(M+1):
#             phi[i,j] = i + j
    pretime = datetime.now()
    while delta > target:
        for i in range(M+1):
            for j in range(M+1):
                if i == 0 or i == M or j == 0 or j == M:
                    phiprime[i,j] = phi[i,j]
                else:
                    phiprime[i, j] = (phi[i+1, j] + phi[i-1, j] \
                                        + phi[i, j+1] + phi[i, j-1])/4
        delta = max(abs(phi-phiprime))
        phi, phiprime = phiprime, phi

    print(datetime.now()-pretime())
    imshow(phi)
    gray()
    show()

if __name__ == "__main__":
    main()