import unittest
import numpy as np
import matplotlib.pyplot as plt

from fft import fft

class TestFft(unittest.TestCase):
    def test_cos_fft(self):
        domain = np.arange(0, np.pi * 9.9, 0.01)
        cos_values = np.cos(domain * 2 * np.pi)
        (fft_freq, fft_values) = fft(cos_values, 0.01)
        plt.plot(fft_freq, fft_values)
        plt.show()

if __name__ == '__main__':
    unittest.main()
