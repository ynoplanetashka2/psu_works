import sympy as sp
import numpy as np
from matplotlib import pyplot as plt
import itertools


def main():
    # f, g = sp.symbols("f g", cls=sp.Function)
    # x = sp.symbols("x")
    # eqs = [sp.Eq(f(x).diff(x), g(x)), sp.Eq(g(x).diff(x), f(x))]
    # sln = sp.dsolve(eqs, [f(x), g(x)], ics={ f(0): 1, g(2): 3 })
    # print(sln)
    # exit()
    t, eta = sp.symbols("t, eta", real=True)
    # x = sp.Function('x', real=True)(t, eta)
    # x_ser = sp.series(x, eta, 0, 4)
    # X0, X1, X2 = sp.Function('X0', real=True)(t), sp.Function('X1', real=True)(t), sp.Function('X2', real=True)(t)
    X0, X1, X2 = sp.symbols("X0, X1, X2", cls=sp.Function, real=True)
    X_arr = [X0(t), X1(t), X2(t)]
    # X0, X1, X2, X3, X4 = sp.symbols('X0, X1, X2, X3, X4', real=True)
    x_ser = X0(t) + X1(t) * eta + X2(t) * eta**2
    # x_ser = X0
    formula = sp.diff(x_ser, t, t) + x_ser + eta * x_ser**3
    expanded = sp.expand(formula).removeO()
    coeffs = sp.Poly(expanded, eta).coeffs()
    coeffs = coeffs[::-1]

    # eqs = list(map(lambda coeff: sp.Eq(coeff, 0), coeffs))
    eqs = coeffs
    solns = []
    for eq in eqs:
        soln = sp.dsolve(
            eq,
            X_arr,
            ics={
                # X0(0): 1,
                # X1(0): 1,
                # X2(0): 1,
                X0(0): (
                    -(
                        sp.diff(X0(t) + X1(t) * eta + X2(t) * eta**2, t, t)
                        + X1(t) * eta
                        + X2(t) * eta**2
                        + eta * (X0(t) + X1(t) * eta + X2(t) * eta**2) ** 3
                    ).subs(t, 0)
                    - 1
                ),
                X0(t)
                .diff(t)
                .subs(t, 0): (
                    (
                        sp.diff(X0(t) + X1(t) * eta + X2(t) * eta**2, t, t)
                        + X1(t) * eta
                        + X2(t) * eta**2
                        + eta * (X0(t) + X1(t) * eta + X2(t) * eta**2) ** 3
                    )
                    .diff(t)
                    .subs(t, 0)
                ),
                # x_ser.diff(t)(0): 0,
            },
        )
        solns.append(soln)
    # print(solns)
    # soln = list(soln)
    # print(soln, len(soln))
    exit()
    soln = list(map(lambda sol: sol.rhs, soln))
    (X0_sub, X1_sub, X2_sub) = soln
    print(X0_sub)
    print(X1_sub)
    print(X2_sub)
    # x_ser = x_ser.replace((X0, X1, X2), (X0_sub, X1_sub, X2_sub))
    x_ser = x_ser.subs([(X0, X0_sub), (X1, X1_sub), (X2, X2_sub)])
    print(x_ser)

    t_range = np.linspace(0.5, 10, 30)
    x_ser = x_ser.subs(eta, 0.1)
    # print(x_ser)
    values = [x_ser.subs(t, t_value) for t_value in t_range]
    # t_range, values = zip(
    #     *filter(
    #         lambda x: (not math.isnan(x[1])) and x[1] < 10_000, zip(k_range, Re_values)
    #     )
    # )
    print(values)
    plt.plot(t_range, values)
    plt.show()


if __name__ == "__main__":
    main()
