import numpy as np
import matplotlib
matplotlib.use('TkAgg')

import matplotlib.pyplot as plt

import scipy.fftpack

# DFFT
def f(t, harmonics):
    v = 0
    for i, harmonic in enumerate(harmonics):
        v += harmonic * np.sin(i * 2.0 * np.pi * t)
    return v

# Number of samplepoints
N = 600
# sample spacing
T = 1.0 / 30.0

t = np.linspace(0.0, N*T, N)
y = f(t, (0, 1.0, 0.6, 0.4, 0.1, 0.1, 0.9))

yf = scipy.fftpack.fft(y)
xf = np.linspace(0.0, 1.0/(2.0*T), N//2)

fig, axarr = plt.subplots(2)
fig.subplots_adjust(hspace=0.5)
axarr[0].plot(t, y)
axarr[0].set_title('Signal')
axarr[1].plot(xf, 2.0/N * np.abs(yf[:N//2]), color='#dd4444')
axarr[1].set_title('Spectrum')
axarr[1].grid(True)
axarr[1].set_xlim(xmin=0)
axarr[1].set_ylim(ymin=0)
axarr[1].set_xticks(np.arange(*axarr[1].get_xlim(), step=1))
axarr[1].set_yticks(np.arange(*axarr[1].get_ylim(), step=0.2))
plt.show()
