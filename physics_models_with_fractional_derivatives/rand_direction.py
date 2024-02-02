import numpy as np
import random

def rand_direction():
    rd = random.random() * 2 * np.pi
    direction = np.array([np.sin(rd), np.cos(rd)])

    return direction
