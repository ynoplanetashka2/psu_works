import unittest
import numpy as np
from autocorrelation import autocorrelation
import matplotlib.pyplot as plt

class TestAutocorrelation(unittest.TestCase):
    def test_cos_transform(self):
        domain = np.linspace(0, np.pi * 10, 100)
        cos_values = np.cos(domain)
        (time, autocorrelation_values) = autocorrelation(cos_values)
        self.assertEqual(autocorrelation_values.size, domain.size)
        plt.plot(cos_values)
        plt.plot(autocorrelation_values)
        plt.show()

if __name__ == '__main__':
    unittest.main()