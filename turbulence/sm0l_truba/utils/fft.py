import numpy as np


def fft(data: np.ndarray, timestep: float):
    measurements_count = data.size
    freq = np.fft.fftfreq(measurements_count, timestep)
    fourier = np.fft.fft(data, measurements_count)
    fourier_abs = (fourier.real**2 + fourier.imag**2) ** (0.5)

    freq_range = freq >= 0.0
    return (freq[freq_range], fourier_abs[freq_range])
