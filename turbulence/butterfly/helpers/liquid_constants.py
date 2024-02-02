BETA_FOR_T = {
    '7': 0.53e-4,
    '15': 1.50e-4,
    '30': 30.2e-4,
    '50': 4.58e-4,
    '70': 5.87e-4,
}

NYU_FOR_T = {
'20': 1.006e-6,
'40': 0.659e-6,
'60': 0.478e-6,
'80': 0.365e-6,

}

LIQUID_CONSTANTS = {
    'RHO': 1_000,
    'C_WATER': 4_200,
    'NYU': NYU_FOR_T['40'],
    'BETA': BETA_FOR_T['30'],
    'HEAT_WIRE_LENGTH': 0.1,
    'N_AVG': 1.33,
    'DN_DT': 0.000_1,
}