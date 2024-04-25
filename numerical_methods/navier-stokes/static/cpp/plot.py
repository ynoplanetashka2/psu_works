import matplotlib.pyplot as plt
import numpy as np
from itertools import islice
import locale
import csv
import os

def main() -> None:
  with open("./Flow1.txt", newline="") as file:
    spamreader = csv.reader(file, delimiter=" ")
    data = []
    data_values = []
    for row in spamreader:
      row = list(
        filter(
          lambda char_: char_ != "", row
          )
        )
      values = list(map(float, row))
      data.append(values)
    data = np.array(data)
    (X, Y, Z) = (data[:, 0], data[:, 1], data[:, 2])
    X = np.unique(X)
    Y = np.unique(Y)
    Z = Z.reshape((X.size, Y.size))
    # Z = np.empty((X.size, Y.size), dtype=float)
    # for i, _ in enumerate(X):
    #   for j, _ in enumerate(Y):
    #     Z[i, j] = data[i, ]

    plt.contour(X, Y, Z, np.linspace(0, 1, 1000))
    plt.show()

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

if __name__ == "__main__":
  main()