import numpy as np
from numpy import linalg
from functools import reduce
import matplotlib.pyplot as plt
from scipy.stats import variation
from datetime import datetime

from avg_displacement import avg_displacements
from diffusion_coef import diffusion_coef

myu_values = np.array([1.5, 2, 3, 4])
dots_count = myu_values.size
jumps_total_count = 10000
repetitions_count = 200
tangent_start_point = 6

tangents = []
plt.xlabel('ln(t)')
plt.ylabel('ln(<r^2>)')
for i in range(dots_count):
    myu = myu_values[i]
    print(f'myu = {myu}')
    _avg_displacements = avg_displacements(myu, jumps_total_count, repetitions_count)
    x_vals = np.log(np.arange(_avg_displacements.size) + 1)
    y_vals = np.log(_avg_displacements + 1)
    tangent, _ = np.polyfit(x_vals[x_vals > tangent_start_point], y_vals[x_vals > tangent_start_point], deg=1)
    tangents.append(tangent)
    print(tangent, myu)
    plt.plot(x_vals, y_vals, label=f'myu = {myu}')

print(tangents, myu_values)
plt.legend()
plt.show()
exit()
#plt.plot(np.log(np.arange(1, iterations_count + 1)), np.log(np.array(avg_displacements)))

for i in range(dots_count):
    diffusions[i] = diffusion_coef(myu_values[i])
    print(i)

print(myu_values, diffusions)
plt.plot(myu_values, diffusions)
#plt.plot(np.arange(1, iterations_count + 1), np.array(avg_displacements))

#delta_r = np.empty(iterations_count - 1, float)
#for i in range(iterations_count - 1):
    #delta = avg_displacements[i + 1] - avg_displacements[i]
    #delta_r[i] = delta

#plt.plot(delta_r)
plt.show()

#output_file = open(f'./out/{datetime.timestamp(datetime.now())}.txt', 'w')
#output_file.write(', '.join(map(str, avg_displacements)))