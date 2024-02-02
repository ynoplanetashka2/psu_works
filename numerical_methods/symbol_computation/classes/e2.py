import sympy as sp
import numpy as np
from matplotlib import pyplot as plt
import itertools

def main():
    t, eta = sp.symbols('t, eta', real=True)
    x = sp.Function('x', real=True)(t, eta)
    # x_ser = sp.series(x, eta, 0, 4)
    X0, X1, X2 = sp.Function('X0', real=True)(t), sp.Function('X1', real=True)(t), sp.Function('X2', real=True)(t)
    X_arr = [X0, X1, X2]
    # X0, X1, X2, X3, X4 = sp.symbols('X0, X1, X2, X3, X4', real=True)
    x_ser = X0 + X1 * eta + X2 * eta**2
    # x_ser = X0
    formula = sp.diff(x_ser, t, t) + x_ser + eta * x_ser ** 3
    expanded = sp.expand(formula).removeO()
    coeffs = sp.Poly(expanded, eta).coeffs()
    coeffs = coeffs[::-1]
    # print('0' * 20)
    # print(f'equations count: {len(coeffs)}')
    # print(coeffs)
    # print('-' * 20)
    # print('0', sp.simplify(coeffs[0].expand()))
    # print('-' * 20)
    # print('1', coeffs[1])
    # print('-' * 20)
    # print('2', coeffs[2])

    eqs = list(map(lambda coeff: sp.Eq(coeff, 0), coeffs))
    # soln = sp.solve(itertools.islice(eqs, len(coeffs)), X_arr)
    # soln = sp.solve((eqs[0], eqs[1], eqs[2]), X_arr, dict=True)
    # print(list(coeffs[0:3]))
    # print(X_arr)
    soln = sp.dsolve(coeffs[0:3], X_arr, x0=(0, 0))
    soln = list(map(lambda sol: sol.rhs, soln))
    print(soln)
    x_ser = x_ser.subs((X0, X1, X2), soln)
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
if __name__ == '__main__':
    main()