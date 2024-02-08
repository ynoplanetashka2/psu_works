import numpy as np

def real_fourier(seq: np.ndarray[float], freq, n):
    result = np.empty(n, float)
    for step in range(n):
        args = np.arange(seq.size)
        result[step] = np.dot(np.cos(args * freq * step), seq)
    return result

def imag_fourier(seq: np.ndarray[float], freq, n):
    result = np.empty(n, float)
    for step in range(n):
        args = np.arange(seq.size)
        result[step] = np.dot(np.sin(args * freq * step), seq)
    return result

def fourier_sq(seq: np.ndarray[float], freq, n):
    result_real = np.empty(n, float)
    result_imag = np.empty(n, float)
    for step in range(n):
        args = np.arange(seq.size)
        result_real[step] = np.dot(np.cos(args * freq * step), seq)
        result_imag[step] = np.dot(np.sin(args * freq * step), seq)
    return result_real ** 2 + result_imag ** 2

def fourier(seq: np.ndarray[float], freq, n):
    return np.sqrt(fourier_sq(seq, freq, n))

def fourier_freq(freq, n):
    return freq / np.arange(n)