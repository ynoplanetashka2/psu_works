import numpy as np
import matplotlib.pyplot as plt

from src.fourier import fourier, fourier_freq, fourier_sq, real_fourier

def main():
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
