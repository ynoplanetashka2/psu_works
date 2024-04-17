import numpy as np

def solve_laplace(field: np.ndarray[float], coordinate_step: float = 1.0) -> np.ndarray[float]:
  shape = field.shape
  equations = np.zeros((shape[0], shape[1], shape[0], shape[1]))
  for i in range(1, shape[0] - 1):
    for j in range(1, shape[1] - 1):
      equations[i, j, i + 1, j] = equations[i, j, i - 1, j] = equations[i, j, i, j + 1] = equations[i, j, i, j - 1] = coordinate_step
      equations[i, j, i, j] = -4 * coordinate_step
  for i in range(shape[0]):
    equations[i, 0, i, 0] = equations[i, -1, i, -1] = 1
  for i in range(shape[1]):
    equations[0, i, 0, i] = equations[-1, i, -1, i] = 1

  soln = np.linalg.tensorsolve(equations, field)
  return soln

def poisson_direct(gridsize,set_boundary):
    A = np.zeros(shape=(gridsize,gridsize,gridsize,gridsize),dtype='d')
    b = np.zeros(shape=(gridsize,gridsize),dtype='d')
    
    dx = 1.0 / (gridsize - 1)
    
    # discretized differential operator
    for i in range(1,gridsize-1):
        for j in range(1,gridsize-1):
            A[i,j,i-1,j] = A[i,j,i+1,j] = A[i,j,i,j-1] = A[i,j,i,j+1] = 1/dx**2
            A[i,j,i,j] = -4/dx**2
    
    # boundary conditions
    for i in range(0,gridsize):
        A[0,i,0,i] = A[-1,i,-1,i] = A[i,0,i,0] = A[i,-1,i,-1] = 1
    
    # set the boundary values on the right side
    set_boundary(b)
    
    return np.linalg.tensorsolve(A,b)