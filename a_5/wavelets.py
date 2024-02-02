from matplotlib.colors import LogNorm
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
data = [np.nditer(samples)]



import numpy as np
from ssqueezepy import cwt
from ssqueezepy.visuals import plot, imshow

#%%# Helper fn + params #####################################################
x = samples

#plot(x, title="x(t) | t=[0, ..., 1], %s samples" % len(x), show=1)

#%%# Take CWT & plot #########################################################
Wx, scales = cwt(x, 'morlet')
imshow(Wx, yticks=scales, abs=1,
       title="abs(CWT) | Morlet wavelet",
       ylabel="scales", xlabel="samples")

