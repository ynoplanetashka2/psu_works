import random as rd
import numpy as np
from scipy.special import zeta

from zeta_values import zeta_values

default_bins_count = int(1e5)

def rand_length(myu, bins_count = default_bins_count):
    (values, sum) = zeta_values(myu, bins_count)
    rand_val = rd.random() * sum
    l = np.searchsorted(values, rand_val)
    return l + 1