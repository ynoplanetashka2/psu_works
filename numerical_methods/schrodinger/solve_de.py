import numpy as np
from scipy.integrate import odeint

def solve_de(domain: np.ndarray[float], eq):
    def equation(y, t):
        (psi_prime, psi) = y
        x = t
        psi_prime_prime = eq(psi, x)
        return (psi_prime_prime, psi_prime)

    solns = odeint(equation, (1, 0), domain)
    psi_prime_soln, psi_soln = solns.T
    return { "psi_soln": psi_soln, "psi_prime_soln": psi_prime_soln }
