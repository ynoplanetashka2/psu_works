import numpy as np


def structure_function(
    first_indicator_values: np.ndarray, second_indicator_values: np.ndarray, myu: float
):
    differences = np.abs(first_indicator_values - second_indicator_values)**myu
    return np.average(differences)
