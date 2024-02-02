from helpers.liquid_constants import LIQUID_CONSTANTS


def l_formula(power):
    #COEFF = 0.0019442018053782456 # old result

    G_EARTH = 9.81
    BETA = LIQUID_CONSTANTS['BETA']
    RHO = LIQUID_CONSTANTS['RHO']
    NYU = LIQUID_CONSTANTS['NYU']
    C_WATER = LIQUID_CONSTANTS['C_WATER']
    HEAT_WIRE_LENGTH = LIQUID_CONSTANTS['HEAT_WIRE_LENGTH']
    COEFF = (G_EARTH * BETA / (2 * RHO * C_WATER * (NYU ** 3) * HEAT_WIRE_LENGTH)) ** (-1 / 3)
    l_value = COEFF * (power ** (-1 / 3))
    return l_value
