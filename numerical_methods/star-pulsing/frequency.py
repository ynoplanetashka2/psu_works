from operator import itemgetter
from solve_pulsing import solve_pulsing
import matplotlib.pyplot as plt
import numpy as np

def get_freq(signal):
    freqs = np.abs(np.fft.fft(signal - signal.mean()))
    max_freq = max(freqs)
    return max_freq

def main():
    N_RANGE = (5, 8, 12, 16)
    freq_values = []
    for n in N_RANGE:
        soln_result = solve_pulsing(n=n, up_to=150, steps_count=100)
        x_soln = itemgetter('x_soln')(soln_result)
        freq = get_freq(x_soln)
        freq_values.append(freq)

    plt.plot(N_RANGE, freq_values)
    plt.show()

if __name__ == "__main__":
    main()