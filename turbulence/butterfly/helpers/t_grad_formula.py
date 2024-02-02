from helpers.liquid_constants import LIQUID_CONSTANTS


def t_grad_formula(epsilon, x_value, power):
    # COEFF = 11.95 # old result
    COEFF = 2 * LIQUID_CONSTANTS['RHO'] * LIQUID_CONSTANTS['C_WATER'] * LIQUID_CONSTANTS['NYU'] * LIQUID_CONSTANTS['N_AVG'] / LIQUID_CONSTANTS['DN_DT']
    return COEFF * epsilon * x_value / power