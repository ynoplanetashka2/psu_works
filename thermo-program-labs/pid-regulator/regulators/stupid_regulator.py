def stupid_regulator(T):
    HE = 0.0
    T_SP = 5
    if T >= T_SP - HE:
        return 0
    return 1