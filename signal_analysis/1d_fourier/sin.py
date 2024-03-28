import numpy as np
from src.continuous_fourier import continuous_fourier
import matplotlib.pyplot as plt

from src.fourier import fourier, fourier_freq, fourier_sq, real_fourier

SIGMA = 13
FREQ = 5
def main():
    #continuous example
    sin = lambda x: np.sin(x)
    identity = lambda x: x
    exp = lambda x: np.exp(-x)
    func = lambda x: np.exp(-(x ** 2 / SIGMA)) * np.sin(FREQ * x)
    func2 = lambda x: np.exp(-(x ** 2 / SIGMA * 3)) * np.sin(FREQ * x)
    transformed_sin = continuous_fourier(sin)
    transformed_identity = continuous_fourier(identity)
    transformed_exp = continuous_fourier(exp)
    transformed_func = continuous_fourier(func)
    transformed_func2 = continuous_fourier(func2)
    freq = np.linspace(1, 10, 100)
    values = np.array([np.abs(transformed_func(arg)) for arg in freq])
    values2 = np.array([np.abs(transformed_func2(arg)) for arg in freq])
    # plt.plot(freq, values * 10)
    # plt.plot(freq, values2 * 10)
    domain = np.linspace(0, 10, 100)
    plt.plot(domain, [func(val) for val in domain])
    plt.plot(domain, [func2(val) for val in domain])
    # plt.xscale("log")
    # plt.yscale("log")
    plt.show()
    exit()
    #discrete example
    _args = np.linspace(0, 10, 1000)
    _sin = np.sin(_args * 2 * np.pi)
    _sin = _sin - _sin.mean()
    res = fourier(_sin, 10, 1000)
    freq = fourier_freq(10, 1000)
    # print(res, freq)
    plt.plot(freq, res)
    # plt.plot(_args, _sin)
    plt.show()

if __name__ == "__main__":
    main()
