def pi_regulator(T_values):
    T = T_values[-1]
    T_SP = 5
    proportional_part = max(0, T_SP - T) / T_SP
    integral_part = 0.005 * (len(T_values) * T_SP - sum(T_values))
    total = proportional_part + integral_part
    return min(1, total)