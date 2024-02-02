import numpy as np

x_values = [
    0,
    0.05,
    0.1,
    0.15,
    0.2,
    0.25,
    0.3,
    0.35,
    0.4,
]

tau_values = [
    1,
    0.832132964,
    0.696398892,
    0.5916897507,
    0.4908587258,
    0.4398891967,
    0.3950138504,
    0.3584487535,
    0.3268698061,
]

L = 0.417

def ls_method(m_value):
    diff = 0
    for (x_value, actual_value) in zip(x_values, tau_values):
        expected = np.cosh(m_value * (L - x_value)) / np.cosh(m_value * L)
        diff += (expected - actual_value)**2
    return diff

m_range = np.arange(3, 5, 0.1)
for m_value in m_range:
    print(f'{m_value:.2f} & {ls_method(m_value):.4f} \\\\')