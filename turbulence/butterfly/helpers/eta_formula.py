from helpers.l_formula import l_formula


def eta_formula(x_value, y_value, power):
    l_value = l_formula(power)
    eta_value = (x_value / l_value) ** (-0.5) * (y_value / l_value)
    return eta_value
