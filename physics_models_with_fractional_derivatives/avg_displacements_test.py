import numpy as np
from numpy.linalg import norm

from avg_displacement import avg_displacements, make_jump_sequence
from rand_displacement import rand_displacement

position_sequences = np.array([[[2, 2], [3, 3]], [[4,4], [1, 1]]])
arr = np.einsum('ijk,ijk->ij', position_sequences, position_sequences)
print(arr)
exit()
print(avg_displacements(1.1, 100, 20).shape)