import numpy as np

def __morlet(sigma: float, t: float) -> float:
    c_sigma = (1 + np.exp(-sigma**2) - 2 * np.exp(-3/4*sigma**2))**(-1/2)
    k_sigma = np.exp(-1/2*sigma**2)
    return c_sigma * np.pi**(-1/4) * np.exp(-1/2*t**2) * (np.exp(1j * sigma * t) - k_sigma)

def morlet_wavelet(length: int, width: float) -> float:
    domain = np.arange(length)
    return [__morlet(width, arg) for arg in domain]