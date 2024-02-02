import numpy as np
from sympy import (
    Eq,
    Poly,
    diff,
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
)
from matplotlib import pyplot as plt


def main():
    a, b, k, Re = symbols("a b k Re", real=True)
    x = symbols("x", real=True)
    w = Function("w")(x)
    teta = Function("teta")(x)
    w_basis = x**2 * (1 - x) ** 2
    teta_basis = x * (1 - x)
    L = (
        diff(w, x, x, x, x)
        - 2 * k**2 * diff(w, x, x)
        + k**4 * w
        - Re * k**2 * teta
    )
    M = diff(teta, x, x) - k**2 * teta + w
    L_substituted = L.subs(w, a * w_basis).subs(teta, b * teta_basis)
    M_substituted = M.subs(w, a * w_basis).subs(teta, b * teta_basis)
    L_int = integrate(simplify(L_substituted * w_basis), (x, 0, 1))
    M_int = integrate(simplify(M_substituted * teta_basis), (x, 0, 1))
    L_int_a_poly_coeffs = Poly(L_int, a).coeffs()
    M_int_a_poly_coeffs = Poly(M_int, a).coeffs()
    coef_matrix = Matrix([L_int_a_poly_coeffs, M_int_a_poly_coeffs])
    soln = solve(Eq(coef_matrix.det(), 0), Re)[0]
    diff_soln = diff(soln, k)
    soln_extrema = solve(Eq(diff_soln, 0), k)
    soln_extrema = list(
        filter(lambda x: x >= 0, map(lambda x: x.evalf(), soln_extrema))
    )
    soln_extrema = soln_extrema[0]
    Re_extrema = soln.subs(k, soln_extrema)

    label = f"k критическое {soln_extrema:.3f}, Re критическое {Re_extrema:.3f}"

    k_range = np.linspace(0.1, 15, 100)
    Re_values = [soln.subs(k, k_value) for k_value in k_range]
    k_range, Re_values = zip(*filter(lambda x: x[1] < 10_000, zip(k_range, Re_values)))
    plt.plot(k_range, Re_values)
    plt.title(label)
    plt.savefig("output/problem1.png")


if __name__ == "__main__":
    main()
