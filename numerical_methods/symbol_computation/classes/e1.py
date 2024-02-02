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
    m, omega, t = symbols("m, omega, t", real=True)
    p = Function("p")(t)
    q = Function("q")(t)
    H = p ** 2 / 2 / m + m * omega ** 2 * q**2 / 2
    H = H.subs((m, 1), (omega, 1))

    eq1 = Eq(diff(q, t), diff(H, p))
    eq2 = Eq(diff(p, t), -diff(H, q))
    res = solve((eq1, eq2), (p, q))
    print(simplify(res))


if __name__ == '__main__':
    main()