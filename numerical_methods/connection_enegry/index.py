import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

def main() -> None:
  ALPHA = 15.56
  BETA = 17.23
  GAMMA = 0.71
  EPSILON = 23.7
  def compute_W(alpha, beta, gamma, epsilon, A, Z) -> float:
    is_A_even = A % 2 == 0
    is_Z_even = Z % 2 == 0
    xi = (+34 if is_Z_even else -34) if is_A_even else 0
    W = alpha * A - beta * A**(2/3) - gamma * Z**2 / A**(1/3) - epsilon * (A - 2 * Z)**2 / A + xi / A**(3/4)
    return W
  Z_domain = np.arange(1, 120)
  A_domain = np.arange(1, 320)
  W_values = np.array([
    [
      compute_W(ALPHA, BETA, GAMMA, EPSILON, A, Z) if A > Z else np.nan
      for A in A_domain] 
    for Z in Z_domain
  ])
  ax = sns.heatmap(W_values)
  W_values_per_nuclon = np.array([
    [
      compute_W(ALPHA, BETA, GAMMA, EPSILON, A, Z) / A if A > Z else np.nan
      for A in A_domain] 
    for Z in Z_domain
  ])
  ax.contour(W_values_per_nuclon, np.linspace(7, 9, 15))
  plt.show()

if __name__ == "__main__":
  main()