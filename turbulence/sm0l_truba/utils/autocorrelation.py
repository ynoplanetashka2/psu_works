import numpy as np


def autocorrelation(data: np.ndarray, step_time=1):
    data = data.copy()
    data = data - data.sum() / data.size
    extropalated_data = np.tile(data, 5)
    autocorrelation_coef_values = np.empty(data.size, float)
    autocorrelation_arg = np.arange(data.size) * step_time
    for n in range(data.size):
        autocorrelation_coef = extropalated_data[:-n] * extropalated_data[n:] if n != 0 else np.power(extropalated_data, 2)
        autocorrelation_coef = autocorrelation_coef.sum()
        autocorrelation_coef /= extropalated_data.size
        autocorrelation_coef_values[n] = autocorrelation_coef
    return (autocorrelation_arg, autocorrelation_coef_values)