import numpy as np

from avg_displacement import avg_displacement

iterations_count = 100
repetitions_count = int(1e2)
def diffusion_coef(myu):
    _avg_displacements = avg_displacements(myu, iterations_count, repetitions_count)
    tangent, _ = np.polyfit(np.arange(_avg_displacements.size), _avg_displacements, deg=1)
    print(_avg_displacements)
    return tangent / 4