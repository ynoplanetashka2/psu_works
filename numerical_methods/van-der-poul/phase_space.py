import numpy as np
import matplotlib.pyplot as plt
import sympy as sp
import scipy as sci
from scipy.integrate import odeint

def main():
    MYU_RANGE = (-1, 0, 1, 2,)
    COLORS = ('black', 'orange', 'yellow', 'green')
    for MYU, COLOR in zip(MYU_RANGE, COLORS):
        def equation(y, t):
            (x_prime, x) = y
            return (MYU * (1 - x**2) * x_prime - x, x_prime)
        domain = np.linspace(0, 1500, 100000)
        solns = odeint(equation, (1, 0), domain)
        x_prime_soln, x_soln = solns.T
        U = x_prime_soln[1:] - x_prime_soln[-1:]
        V = x_soln[1:] - x_soln[-1:]
        plt.quiver(x_prime_soln[:-1], x_soln[:-1], U, V, color=COLOR, label=f'myu: {MYU}')

    plt.legend()
    plt.show()


if __name__ == '__main__':
    main()
