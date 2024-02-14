import numpy as np
import matplotlib.pyplot as plt

def main():
    P_d = 0.01
    I = np.eye(2)
    SIGMA_x = np.array([[0, 1], [1, 0]])
    SIGMA_y = np.array([[0, -(0 + 1j)], [(0 + 1j), 0]])
    SIGMA_z = np.array([[1, 0], [0, -1]])
    SIGMA_VALUES = np.array([SIGMA_x, SIGMA_y, SIGMA_z])
    S_VALUES = [
        [None for _ in range(3)] for _ in range(3)
    ]
    for alpha in range(3):
        for pos in range(3):
            operations = [I, I, I]
            operations[pos] = SIGMA_VALUES[alpha]
            S_VALUES[alpha][pos] = np.kron(operations[0], np.kron(operations[1], operations[2]))
    S_VALUES = np.array(S_VALUES)
    (S_PLUS_VALUES, S_MINUS_VALUES) = (operation(S_VALUES[0], S_VALUES[1]) for operation in (lambda x, y: x + y, lambda x, y: x - y))
    zeeman = 0
    for j in range(3):
        zeeman += S_VALUES[2][j]
    dipol = 0
    for j in range(3):
        for k in range(3):
            if j == k:
                continue
            dipol += - P_d / 2 * (S_VALUES[2][j] * S_VALUES[2][k] - 1/4 * (S_PLUS_VALUES[j] * S_MINUS_VALUES[k] + S_MINUS_VALUES[j] * S_PLUS_VALUES[k]))
    total = zeeman + dipol
    
    eigh = np.linalg.eigh(total)
    print(f'{eigh=}')

if __name__ == "__main__":
    main()