import matplotlib.pyplot as plt
import numpy as np
from numpy import pi, sin, cos
import scipy.integrate
from scipy import signal
from scipy.io import wavfile

sample_rate, samples = wavfile.read('camerton.wav')
samples = samples.astype(float)
#samples = samples[100000:101000]
samples = samples[:, 0]
samples_max = np.max(samples)
samples /= samples_max
samples_count = samples.shape[0]
samples_domain = np.arange(samples_count, dtype = float) #/ sample_rate

#print(sample_rate)
#print(samples)

#plt.plot(samples)
#plt.show()
#quit()
#frequencies, times, spectrogram = signal.spectrogram(samples, sample_rate)

#print(times)
#print(frequencies)
#print(spectrogram)
#plt.pcolormesh(times, frequencies, spectrogram)
def get_fourier(mapping, items_count):
    indexes = []
    domain = mapping[:, 0]
    image = mapping[:, 1]
    for n in range(items_count):
        cos_filter = cos(n * domain)
        sin_filter = sin(n * domain)
        cos_mapping = image * cos_filter
        sin_mapping = image * sin_filter
        #print(cos_mapping, cos_mapping.size)
        #print(np.sum(cos_mapping))
        a_n = 1 / pi * np.sum(cos_mapping)
        b_n = 1 / pi * np.sum(sin_mapping)

        indexes.append((a_n, b_n))
    return indexes

_, ax = plt.subplots()

_map = np.empty((samples_count, 2))
_map[:, 1] = samples
_map[:, 0] = samples_domain
fourier = get_fourier(_map, 500)
squares_sum = [a**2 + b**2 for (a, b) in fourier]
squares_sum_indexes = [index / sample_rate * 2 * pi for (index, _) in enumerate(fourier)]
ax.plot(squares_sum_indexes, squares_sum)
ax.set_xlabel('[sec]')
#ax.set_xlabel(np.array(samples_domain))
#plt.plot(samples)
#print(fourier)
#mapping = fourier
#plt.plot(fourier)
plt.show()
