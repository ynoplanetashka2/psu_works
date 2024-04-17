import numpy as np

def _U(x):
  U_0 = 1
  return U_0 * np.abs(x)


def create_schrodinger_equation(E: float):
  h = 1.05e-27 / 1.6e-12
  m = 9.1e-28
  psi_prime_prime_coeff = - h**2 / m
  def schrodinger_equation(psi: float, x: float) -> float:
    result = (E - _U(x)) / psi_prime_prime_coeff * psi
    return result
  return schrodinger_equation
  
