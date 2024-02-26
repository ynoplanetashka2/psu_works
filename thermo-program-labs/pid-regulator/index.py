from setup_window import setup_window
from regulators.stupid_regulator import stupid_regulator

T_INI = 0

def main():
    setup_window(compute_p=stupid_regulator, T_INI=T_INI)

if __name__ == "__main__":
    main()