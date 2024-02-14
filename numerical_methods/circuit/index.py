import numpy as np
import matplotlib.pyplot as plt

def main():
    def compute(omega):
        E_abs = 1
        R_1 = 1
        R_h = 50
        L = 1 * 1e-6
        C = 1_000 * 1e-12
        X_1 = R_1
        X_h = R_h
        L_imp = (0 + 1j) * omega * L
        C_imp = - (0 + 1j) / ( omega * C )

        C_and_X_h_imp = 1 / (1 / C_imp * 1 / X_h)
        X1_and_L_imp = X_1 + L_imp
        total_imp = C_and_X_h_imp + X1_and_L_imp
        abs_current = abs(E_abs / total_imp)
        X1_and_L_charge = abs_current * abs(X1_and_L_imp)
        C_and_X_h_charge = E_abs - X1_and_L_charge
        return C_and_X_h_charge
    
    OMEGA_RANGE = np.linspace(1, 1e6, 20)
    values = np.array([compute(omega) for omega in OMEGA_RANGE])
    plt.plot(OMEGA_RANGE, values)
    plt.show()


if __name__ == "__main__":
    main()