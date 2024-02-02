def epsilon_formula(epsilon_shift):
    # фокусное расстояние в метрах
    FOCUS_DISTANCE = 1.2
    COEFF = 1 / FOCUS_DISTANCE
    epsilon_value = COEFF * epsilon_shift
    return epsilon_value
