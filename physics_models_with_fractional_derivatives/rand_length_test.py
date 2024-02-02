import numpy as np
import matplotlib.pyplot as plt
import scipy.special

from rand_length import rand_length
from zeta_values import zeta_values

myu = 1.5
bins_count = 100000
#print(scipy.special.zeta(myu))
#print(zeta_values(myu, bins_count)[1])
#exit()

iterations_count = int(1e5)
length_values = np.empty(iterations_count)
for i in range(iterations_count):
    length_values[i] = rand_length(myu, bins_count)

bins = np.empty(bins_count, float)
for i in range(bins_count):
    bins[i] = length_values[length_values == (i + 1)].size
bins /= iterations_count
accurate_values = (scipy.special.zeta(myu))**(-1) * (np.arange(bins_count, dtype=float) + 1)**(-myu)
differencies = bins - accurate_values
print(np.abs(differencies))
print(np.abs(differencies).sum())
