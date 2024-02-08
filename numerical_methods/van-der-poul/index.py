import numpy as np
import matplotlib.pyplot as plt
import sympy as sp

def main():
    t, myu = sp.symbols('t, myu', real=True)
    x_bare = sp.symbols('x', cls=sp.Function, real=True)
    x = x_bare(t)
    eq = x.diff(t, 2) - myu * (1 - x ** 2) * x.diff(t) + x
    soln = sp.dsolve(eq, x, ic={ 
        x_bare(0): 1, 
        x_bare.diff(t).subs(t, 0): 0
    })
    print(soln)

if __name__ == '__main__':
    main()