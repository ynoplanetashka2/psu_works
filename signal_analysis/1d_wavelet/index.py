from src.morlet_wavelet import morlet_wavelet
from scipy.signal import cwt
import numpy as np
import matplotlib.pyplot as plt
import pywt as wt

def main():
    domain = np.arange(480)
    left_half  = domain[:250]
    right_half = domain[250:]
    left_values = np.sin(2 * np.pi * left_half / 32)
    right_values = np.sin(3 * np.pi * right_half / 32)
    values = np.concatenate((left_values, right_values))
    widths = np.arange(1, 46)
    cwmatr, freqs = wt.cwt(values, widths, "morl")
    # plt.imshow(cwmatr, extent=[-1, 1, 1, 31], cmap="PRGn", aspect="auto")
    plt.matshow(cwmatr)
    # plt.plot(coefs, freqs)
    plt.show()

if __name__ == "__main__":
    main()