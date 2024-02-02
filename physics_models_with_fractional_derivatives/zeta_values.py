from functools import cache
from itertools import count
import numpy as np

@cache
def zeta_values(myu, bins_count):
    values = np.empty(bins_count, float)
    last_value = 0
    for n in range(bins_count):
        term = 1 / (n + 1)**myu
        last_value += term
        values[n] = last_value

    sum = values[-1]
    
    return (values, sum)