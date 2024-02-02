from rand_direction import rand_direction
from rand_length import rand_length

def rand_displacement(myu):
    direction = rand_direction()
    length = rand_length(myu)

    res = direction * length
    
    return res