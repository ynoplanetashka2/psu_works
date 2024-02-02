from helpers.l_formula import l_formula

from helpers.liquid_constants import LIQUID_CONSTANTS

def T_formula(x_value, t_value, power):
    #COEFF = 1.2 # old result
    COEFF = 1 / (2 * LIQUID_CONSTANTS['RHO'] * LIQUID_CONSTANTS['C_WATER'] * LIQUID_CONSTANTS['NYU'] * LIQUID_CONSTANTS['HEAT_WIRE_LENGTH'])
    l_value = l_formula(power)
    T_value = COEFF * power * (x_value / l_value) ** (-1 / 2) * t_value
    return T_value
