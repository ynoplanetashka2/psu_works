import matplotlib.pyplot as plt
from scipy import special as spec
from matplotlib.animation import FuncAnimation
import numpy as np

def main():
  fig = plt.figure()
  ax = fig.add_subplot(projection='3d')

  # Set an equal aspect ratio
  ax.set_aspect('equal')

  def update(frame):
    DELTA_R = 0.2
    HARMONIC_ORDER = 2
    HARMONIC_DEGREE = 3
    OMEGA = 2 * np.pi
    time = frame
    # Make data
    u = np.linspace(0, 2 * np.pi, 100)
    v = np.linspace(0, np.pi, 100)
    spherical = spec.sph_harm(HARMONIC_ORDER, HARMONIC_DEGREE, u, v)
    radius = 1 + DELTA_R * np.sin(OMEGA * time) * spherical
    x = radius * np.outer(np.cos(u), np.sin(v))
    y = radius * np.outer(np.sin(u), np.sin(v))
    z = radius * np.outer(np.ones(np.size(u)), np.cos(v))
    # Plot the surface
    ax.clear()
    ax.plot_surface(x, y, z)

  update(0)
  _ = FuncAnimation(fig, update, frames=np.linspace(0, 10, 100), interval=50)
  plt.show()

if __name__ == "__main__":
  main()