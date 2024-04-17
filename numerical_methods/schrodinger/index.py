import matplotlib.pyplot as plt
import numpy as np
from equaion import create_schrodinger_equation
from solve_de import solve_de


def main():
  E_range = np.linspace(3, 10, 5)
  for E in E_range:
    print(f"{E=}")
    schrodinger_equation = create_schrodinger_equation(E)
    domain = np.linspace(-3e-0, +3e-0, 100)
    soln = solve_de(domain, schrodinger_equation)
    psi_soln = soln["psi_soln"]
    plt.plot(domain, psi_soln, label=f"{E=}")
  plt.legend(loc="upper left")
  plt.show()

if __name__ == "__main__":
  main()