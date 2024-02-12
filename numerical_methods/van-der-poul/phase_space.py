from operator import itemgetter
import numpy as np
from solve_van_der_poul import solve_van_der_poul
import matplotlib.pyplot as plt
import sympy as sp
import scipy as sci
from scipy.integrate import odeint

def main():
    MYU_RANGE = (0, 1, 2,)
    COLORS = ('black', 'orange', 'yellow', 'green')
    for MYU, COLOR in zip(MYU_RANGE, COLORS):
        soln_result = solve_van_der_poul(myu=MYU, up_to=1500, steps_count=10000)
        x_soln, x_prime_soln = itemgetter('x_soln', 'x_prime_soln')(soln_result)
        U = x_prime_soln[1:] - x_prime_soln[-1:]
        V = x_soln[1:] - x_soln[-1:]
        plt.quiver(x_prime_soln[:-1], x_soln[:-1], U, V, color=COLOR, label=f'myu: {MYU}')

    plt.legend()
    plt.show()


if __name__ == '__main__':
    main()
