import numpy as np
from operator import itemgetter
from scipy.integrate import odeint


def solve_van_der_poul(**kwargs):
    myu, up_to, steps_count = itemgetter("myu", "up_to", "steps_count")(kwargs)

    def equation(y, t):
        (x_prime, x) = y
        return (myu * (1 - x**2) * x_prime - x, x_prime)

    domain = np.linspace(0, up_to, steps_count)
    solns = odeint(equation, (1, 0), domain)
    x_prime_soln, x_soln = solns.T
    return {"domain": domain, "x_soln": x_soln, "x_prime_soln": x_prime_soln}
