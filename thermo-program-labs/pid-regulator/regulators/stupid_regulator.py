def stupid_regulator(T_values):
    T = T_values[-1]
    HE = 0.0
    T_SP = 5
    if T >= T_SP - HE:
        return 0
    return 1