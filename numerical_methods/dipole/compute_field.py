import numpy as np

SIGMA = 0.8
CHARGE_DISTNACE = 1
SPEED_OF_LIGHT = 1
X_GRID, Y_GRID = np.meshgrid(np.linspace(0, 40, 100), np.linspace(0, 40, 100))

def compute_field(q, x0, y0):
    return q / np.sqrt(2 * np.pi) / SIGMA * np.exp(- ((X_GRID - x0)**2 + (Y_GRID - y0)**2) / (2 * SIGMA**2)) * 5