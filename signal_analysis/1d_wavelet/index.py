from src.morlet_wavelet import morlet_wavelet
from scipy.signal import cwt
import numpy as np
import matplotlib.pyplot as plt
import pywt as wt

def main():
    domain = np.arange(480)
    values = (
        np.sin((0.5 + domain / 1000) * np.pi * domain / 8)
        + np.sin((1 - domain / 1000) * np.pi * domain / 8)
    )
    widths = np.arange(1, 80)
    cwmatr, freqs = wt.cwt(values, widths, "morl")
    plt.matshow(cwmatr)
    plt.show()

if __name__ == "__main__":
    main()