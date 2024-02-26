def proportional_regulator(T_values):
    T = T_values[-1]
    T_SP = 5
    return max(0, T_SP - T) / T_SP
