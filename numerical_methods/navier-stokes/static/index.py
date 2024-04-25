import numpy as np
import datetime
import os
import matplotlib.pyplot as plt

def solve_poissons(field: np.ndarray[float], coordinate_step: float = 1.0, relaxation_parameter: float = 1.0, iterations_limit: int = 100_000, accuracy: float = 1e-1) -> np.ndarray[float]:
  # shape = field.shape
  # equations = np.zeros((shape[0], shape[1], shape[0], shape[1]))
  # for i in range(1, shape[0] - 1):
  #   for j in range(1, shape[1] - 1):
  #     equations[i, j, i + 1, j] = equations[i, j, i - 1, j] = equations[i, j, i, j + 1] = equations[i, j, i, j - 1] = coordinate_step
  #     equations[i, j, i, j] = -4 * coordinate_step
  # for i in range(shape[0]):
  #   equations[i, 0, i, 0] = equations[i, -1, i, -1] = 1
  # for i in range(shape[1]):
  #   equations[0, i, 0, i] = equations[-1, i, -1, i] = 1

  # soln = np.linalg.tensorsolve(equations, field)
  # return soln
  # for i in range(shape[0]):
  #   soln[i, 0] = field[i, 0]
  #   soln[i, -1] = field[i, -1]
  # for i in range(shape[1]):
  #   soln[0, i] = field[0, i]
  #   soln[-1, i] = field[-1, i]
  shape = field.shape
  soln = np.zeros(shape)
  next_soln = np.zeros(shape)
  soln[1, 1] = 1e-6
  for _ in range(iterations_limit):
    for i in range(1, shape[0] - 1):
      for j in range(1, shape[1] - 1):
        next_soln[i, j] += relaxation_parameter / 4 * (soln[i + 1, j] + soln[i - 1, j] + soln[i, j + 1] + soln[i, j - 1] - coordinate_step**2 * field[i, j]) - relaxation_parameter * soln[i, j]
    soln = next_soln.copy()
    if (np.abs(soln - field) < accuracy).all():
      print("poissons solved")
      return soln[1:-1, 1:-1]
    # else:
    #   print(f"not solved for {_}")
  raise Exception(f"iterations count exceed limit: {iterations_limit}")

def main() -> None:
  UP_TO_TIME = 10
  LATTICE_SIZE = 20
  RE = 10
  COORDINATE_STEP = 1 / (LATTICE_SIZE - 1)
  TIME_STEP = COORDINATE_STEP**2 / (4 * RE) / 2
  SNAPSHOTS_COUNT = 800
  fi_values = np.zeros((LATTICE_SIZE, LATTICE_SIZE))
  fi_values[10, 10] = 1e-5
  psi_values = np.zeros((LATTICE_SIZE, LATTICE_SIZE))
  psi_values = np.zeros((LATTICE_SIZE, LATTICE_SIZE))
  psi_values[10, 10] = 1e-5
  next_fi_values = np.zeros((LATTICE_SIZE, LATTICE_SIZE))
  next_psi_values = np.zeros((LATTICE_SIZE, LATTICE_SIZE))
  total_iterations_count = int(UP_TO_TIME / TIME_STEP)
  print(f"{total_iterations_count=}")
  now = datetime.datetime.now()
  now_int = int(now.strftime("%Y%m%d%H%M%S"))
  snapshots_dir_path = f"snapshots/at_{now_int}"
  os.mkdir(snapshots_dir_path)
  
  def make_snapshot():
    velocity = np.zeros((LATTICE_SIZE, LATTICE_SIZE, 2))
    for i in range(LATTICE_SIZE - 1):
      for j in range(LATTICE_SIZE - 1):
        psi_x_derivative = (psi_values[i + 1, j] - psi_values[i, j]) / COORDINATE_STEP
        psi_y_derivative = (psi_values[i, j + 1] - psi_values[i, j]) / COORDINATE_STEP
        velocity[i, j] = np.array([psi_y_derivative, -psi_x_derivative])
    x_coords = np.linspace(0, 1, LATTICE_SIZE)
    y_coords = np.linspace(0, 1, LATTICE_SIZE)
    fig, ax = plt.subplots()
    ax.quiver(x_coords, y_coords, velocity[:,:,0], velocity[:,:,1])
    fig.savefig(f"{snapshots_dir_path}/snapshot_{current_time:.3f}.png")
    print(f"snapshot for {current_time=} ({current_iteration=})")

  for current_time in np.arange(0, UP_TO_TIME, TIME_STEP):
    current_iteration = int(current_time / TIME_STEP)
    for i in range(1, len(fi_values) - 1):
      for j in range(1, len(fi_values) - 1):
        fi_x_derivative = (fi_values[i + 1, j] - fi_values[i, j]) / COORDINATE_STEP
        fi_y_derivative = (fi_values[i, j + 1] - fi_values[i, j]) / COORDINATE_STEP
        laplace_fi = (
          (fi_values[i + 1, j] - 2 * fi_values[i, j] + fi_values[i - 1, j]) / COORDINATE_STEP**2
          + (fi_values[i, j + 1] - 2 * fi_values[i, j] + fi_values[i, j - 1]) / COORDINATE_STEP**2
        )
        psi_x_derivative = (psi_values[i + 1, j] - psi_values[i, j]) / COORDINATE_STEP
        psi_y_derivative = (psi_values[i, j + 1] - psi_values[i, j]) / COORDINATE_STEP
        next_fi_values[i][j] += TIME_STEP * (
          (psi_x_derivative * fi_y_derivative - psi_y_derivative * fi_x_derivative)
          + 1 / RE * laplace_fi
        )
    psi_field = np.zeros((next_fi_values.shape[0] + 2, next_fi_values.shape[1] + 2))
    psi_field[1:-1, 1:-1] = -next_fi_values
    next_psi_values = solve_poissons(psi_field, COORDINATE_STEP)
    for i in range(len(fi_values)):
      next_fi_values[i, 0] = 2 / COORDINATE_STEP**2 * next_psi_values[i, 1]
      next_fi_values[0, i] = 2 / COORDINATE_STEP**2 * next_psi_values[1, i]
      next_fi_values[-1, i] = 2 / COORDINATE_STEP**2 * next_psi_values[-2, i]
      next_fi_values[i, -1] = 2 / COORDINATE_STEP**2 * next_psi_values[i, -2] - 2 / COORDINATE_STEP
    
    next_fi_values_has_nan = np.isnan(next_fi_values).any()
    next_psi_values_has_nan = np.isnan(next_psi_values).any()
    if next_fi_values_has_nan or next_psi_values_has_nan:
      print(f"error occuried at time {current_time=} (iteration {int(current_time / TIME_STEP)})")
      print(f"{next_fi_values_has_nan=} {next_psi_values_has_nan=}")
      exit(1)

    fi_values, psi_values = (next_fi_values.copy(), next_psi_values.copy())

    if current_iteration % int(total_iterations_count / SNAPSHOTS_COUNT) == 0:
      if current_iteration == 0:
        continue
      make_snapshot()

if __name__ == "__main__":
  main()