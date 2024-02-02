from functools import reduce
from numpy.linalg import norm
import numpy as np
from numpy import linalg

from rand_displacement import rand_displacement


def make_jump_sequence(position, jumps_count, myu):
    position = position.copy()
    for i in range(jumps_count):
        _rand_displacement = rand_displacement(myu)
        position += _rand_displacement
    return position

def make_jump(position, myu):
    return make_jump_sequence(position, 1, myu)

def generate_positions_sequence(total_jumps_count, myu):
    positions = np.empty((total_jumps_count, 2), float)
    positions[0] = np.array([0, 0], float)
    for i in range(1, total_jumps_count):
        positions[i] = make_jump(positions[i - 1], myu)
    return positions

def total_displacement(myu, jumps_count):
    displacements = np.array([rand_displacement(myu) for _ in range(jumps_count)])
    _total_displacement = displacements.sum(axis=0)
    return np.dot(_total_displacement, _total_displacement)

def avg_displacement(myu, jumps_count, repetitions_count):
    """average displacement 
    """
    total_displacements = np.empty(repetitions_count, float)
    for i in range(repetitions_count):
        displacement = total_displacement(myu, jumps_count)
        total_displacements[i] = displacement

    avg_displacement = total_displacements.mean()
    return avg_displacement

def avg_displacements(myu, jumps_total_count, repetitions_count):
    """average displacements up to jumps_total_count for certian myu and repetitions count
    """
    position_sequences = [generate_positions_sequence(jumps_total_count, myu) for _ in range(repetitions_count)]
    position_sequences = np.array(position_sequences)
    _avg_displacements = np.einsum('ijk,ijk->ij', position_sequences, position_sequences)
    #_avg_displacements = np.norm(position_sequences, axis=2)
    #_avg_displacements[,,:] = _avg_displacements[,,:]**2
    _avg_displacements = _avg_displacements.mean(axis=0)
    return _avg_displacements