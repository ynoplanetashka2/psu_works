import numpy as np
from sympy import (
    Eq,
    Poly,
    diff,
    exp,
    sin,
    cos,
    solve,
    symbols,
    integrate,
    Matrix,
    latex,
    Function,
    simplify,
    expand,
    factor,
)
from sympy.calculus.util import minimum, Interval
from matplotlib import pyplot as plt
import math


def main():
    a, k, Ra = symbols("a k Ra", real=True, positive=True)
    z = symbols("z", real=True, positive=True)
    w_input = Function("w_input")(z)
    teta_input = Function("teta_input")(z)
    w_basis = z**2 * (1 - z) ** 2
    w = a * w_basis

    A = (
        a
        * 2
        * (exp(-k) * k**2 - k**2 + 12 * exp(-k) - 12)
        / (k**6 * (exp(k) - exp(-k)))
    )
    B = (
        a
        * (-2)
        * (exp(k) * k**2 - k**2 + 12 * exp(k) - 12)
        / (k**6 * (exp(k) - exp(-k)))
    )
    C_1 = a / k**2
    C_2 = -2 * a / k**2
    C_3 = a * (k**2 + 12) / k**4
    C_4 = -12 * a / k**4
    C_5 = 2 * a * (k**2 + 12) / k**6
    teta_1 = A * exp(k * z) + B * exp(-k * z)
    teta_2 = C_1 * z**4 + C_2 * z**3 + C_3 * z**2 + C_4 * z + C_5
    teta = simplify(teta_1 + teta_2)

    L = (
        diff(w_input, z, z, z, z)
        - 2 * k**2 * diff(w_input, z, z)
        + k**4 * w
        - Ra * k**2 * teta_input
    )
    L_substituted = L.subs(w_input, w).subs(teta_input, teta)
    L_substituted = simplify(L_substituted)
    L_product = simplify(L_substituted * w_basis / a)
    L_int = integrate(L_product, (z, 0, 1))
    soln = solve(Eq(L_int, 0), Ra)[0]
    soln_args = np.linspace(2.5, 4, 40)
    soln_points = [soln.subs(k, arg) for arg in soln_args]
    soln_points = np.array(soln_points)
    arg_max = soln_points.argmin()
    soln_extrema = soln_args[arg_max]
    Re_extrema = soln_points[arg_max]
    print(f"k критическое: {soln_extrema:.3f}, Re критическое: {Re_extrema:.3f}")

    k_range = np.linspace(0.5, 10, 30)
    Re_values = [soln.subs(k, k_value) for k_value in k_range]
    k_range, Re_values = zip(
        *filter(
            lambda x: (not math.isnan(x[1])) and x[1] < 10_000, zip(k_range, Re_values)
        )
    )
    plt.plot(k_range, Re_values)
    plt.show()


if __name__ == "__main__":
    main()
