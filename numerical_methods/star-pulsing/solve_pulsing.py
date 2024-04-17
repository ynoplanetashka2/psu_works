import numpy as np
from operator import itemgetter
from scipy.integrate import odeint
from equation import star_pulsing_for_n

def solve_pulsing(**kwargs):
    n, up_to, steps_count = itemgetter("n", "up_to", "steps_count")(kwargs)
    eq = star_pulsing_for_n(n)

    def equation(y, t):
        (r_prime, r) = y
        return (eq(r, r_prime), r_prime)

    domain = np.linspace(0, up_to, steps_count)
    solns = odeint(equation, (1.01, 0), domain)
    print(solns.shape)
    x_prime_soln, x_soln = solns.T
    print(x_prime_soln.shape, x_soln.shape)
    return {"domain": domain, "x_soln": x_soln, "x_prime_soln": x_prime_soln}
