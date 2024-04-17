from operator import itemgetter
from solve_pulsing import solve_pulsing
import matplotlib.pyplot as plt

def main():
    N_RANGE = (5, 8, 12, 16)
    COLORS = ('black', 'orange', 'yellow', 'green')
    for n, COLOR in zip(N_RANGE, COLORS):
        soln_result = solve_pulsing(n=n, up_to=10, steps_count=1000)
        x_soln, x_prime_soln = itemgetter('x_soln', 'x_prime_soln')(soln_result)
        U = x_prime_soln[1:] - x_prime_soln[-1:]
        V = x_soln[1:] - x_soln[-1:]
        plt.quiver(x_prime_soln[:-1], x_soln[:-1], U[::-1], V[::-1], color=COLOR, label=f'n: {n}')

    plt.legend()
    plt.show()


if __name__ == '__main__':
    main()
