from operator import itemgetter
from solve_van_der_poul import solve_van_der_poul
import matplotlib.pyplot as plt
import numpy as np

def get_freq(signal):
    freqs = np.abs(np.fft.fft(signal - signal.mean()))
    max_freq = max(freqs)
    return max_freq

def main():
    MYU_RANGE = np.linspace(0, 2, 50)
    freq_values = []
    for MYU in MYU_RANGE:
        soln_result = solve_van_der_poul(myu=MYU, up_to=150, steps_count=100)
        x_soln = itemgetter('x_soln')(soln_result)
        freq = get_freq(x_soln)
        freq_values.append(freq)

    plt.plot(MYU_RANGE, freq_values)
    plt.show()

if __name__ == "__main__":
    main()