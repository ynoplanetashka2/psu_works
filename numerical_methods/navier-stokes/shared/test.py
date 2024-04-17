import numpy as np
import matplotlib.pyplot as plt
from solve_laplace import solve_laplace

def main() -> None:
  LATTICE = 100
  base = [[np.sin(x*y) for y in range(LATTICE)] for x in range(LATTICE)]
  base = -np.array(base)
  soln = solve_laplace(base)
  plt.imshow(soln, cmap="hot")
  plt.show()

if __name__ == "__main__":
  main()

