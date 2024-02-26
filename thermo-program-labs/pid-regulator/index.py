from setup_window import setup_window
from regulators.stupid_regulator import stupid_regulator

def main():
    setup_window(compute_p=stupid_regulator)

if __name__ == "__main__":
    main()