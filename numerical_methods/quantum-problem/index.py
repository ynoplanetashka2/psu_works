import numpy as np
from functools import reduce
import matplotlib.pyplot as plt


def main():
    P_d = 0.01
    I = np.eye(2)
    SIGMA_x = np.array([[0, 1], [1, 0]])
    SIGMA_y = np.array([[0, -(0 + 1j)], [(0 + 1j), 0]])
    SIGMA_z = np.array([[1, 0], [0, -1]])
    SIGMA_VALUES = np.array([SIGMA_x, SIGMA_y, SIGMA_z])
    S_VALUES = [[None for _ in range(3)] for _ in range(3)]
    for alpha in range(3):
        for pos in range(3):
            operations = [I, I, I]
            operations[pos] = SIGMA_VALUES[alpha]
            S_VALUES[alpha][pos] = np.kron(
                operations[0], np.kron(operations[1], operations[2])
            )
    S_VALUES = np.array(S_VALUES)
    (S_PLUS_VALUES, S_MINUS_VALUES) = (
        operation(S_VALUES[0], S_VALUES[1])
        for operation in (lambda x, y: x + y, lambda x, y: x - y)
    )
    zeeman = 0
    for j in range(3):
        zeeman += S_VALUES[2][j]
    dipol = 0
    for j in range(3):
        for k in range(3):
            if j == k:
                continue
            dipol += (
                -P_d
                / 2
                * (
                    S_VALUES[2][j] * S_VALUES[2][k]
                    - 1
                    / 4
                    * (
                        S_PLUS_VALUES[j] * S_MINUS_VALUES[k]
                        + S_MINUS_VALUES[j] * S_PLUS_VALUES[k]
                    )
                )
            )
    total = zeeman + dipol
    print(f"{(dipol != 0)=}")

    eigh = np.linalg.eigh(total)
    print(f"{eigh=}")
    exit()
    (ZERO_ORDER_EIGH_VALS, ZERO_ORDER_EIGH_VECTORS) = eigh

    PERTURBATION_ABS = 1e-2
    PERTURBATION = np.random.random((8, 8)) * PERTURBATION_ABS
    FIRST_ORDER_EIGH_VALS = np.array(
        [
            np.dot(eigh_vector, np.matmul(PERTURBATION, eigh_vector))
            for eigh_vector in ZERO_ORDER_EIGH_VECTORS
        ]
    )
    FIRST_ORDER_EIGH_VECTORS = np.zeros(ZERO_ORDER_EIGH_VECTORS.shape)
    for n, eigh_vec_n, eigh_val_n in zip(range(ZERO_ORDER_EIGH_VECTORS.shape[0]), ZERO_ORDER_EIGH_VECTORS, ZERO_ORDER_EIGH_VALS):
        sum_ = np.zeros(ZERO_ORDER_EIGH_VECTORS.shape[1])
        for m, eigh_vec_m, eigh_val_m in zip(range(ZERO_ORDER_EIGH_VECTORS.shape[0]), ZERO_ORDER_EIGH_VECTORS, ZERO_ORDER_EIGH_VALS):
            if m == n:
                continue
            enumerator = np.dot(eigh_vec_m, np.matmul(PERTURBATION, eigh_vec_n))
            denominator = eigh_val_n - eigh_vec_m
            sum_ += enumerator / denominator * eigh_vec_m
        FIRST_ORDER_EIGH_VECTORS[n] = sum_


if __name__ == "__main__":
    main()
