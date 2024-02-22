from scipy import integrate
import numpy as np

def continuous_fourier(func):
    def transformed(fi):
        (real_part, _) = integrate.quad(lambda t: np.cos(fi * t) * func(t), 0, float('inf'))
        (imaginary_part, _) = integrate.quad(lambda t: np.sin(fi * t) * func(t), 0, float('inf'))
        return real_part + 1j * imaginary_part
    return transformed