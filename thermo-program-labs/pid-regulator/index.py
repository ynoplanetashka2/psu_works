from setup_window import setup_window
from regulators.positional_regulator import positional_regulator
from regulators.proportional_regulator import proportional_regulator
from regulators.pi_regulator import pi_regulator

T_INI = 0

def main():
    setup_window(compute_p=pi_regulator, T_INI=T_INI)

if __name__ == "__main__":
    main()