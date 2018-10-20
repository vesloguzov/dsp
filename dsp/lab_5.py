import numpy as np
import math
from scipy import signal
import matplotlib.pyplot as plt, mpld3
from utils import save_stem

fd = 100
f0 = 23  # np.floor(50*np.random.uniform(0, 1))

s = np.cos(2 * math.pi * f0 * (np.arange(fd)) / fd)
K = np.array([2, 4, 5])
K_e = 4 #np.random.choice(K)

s1 = s[0::K_e]

m1, mi = abs(np.fft.fft(s1)).max(0), abs(np.fft.fft(s1)).argmax(0)+1

fn_et = fd*mi/len(s1)

# plt.stem(abs(np.fft.fft(s)), 'c')
# plt.show()
# plt.close()
# plt.stem(abs(np.fft.fft(s1)), 'c')
# plt.show()
# plt.close()

T = 10
fe = 0
fs = 20

sl = signal.chirp(np.arange(0.01, T + 0.01, 0.01), 0, T, fs)

K = 6

slc = sl[0::K]
Np = math.pow(100, 2.0) / math.pow(K, 2) * T / fs

# plt.plot(np.abs(np.diff(np.diff(np.diff(np.diff(np.diff(slc)))))))
# plt.show()
# plt.close()

# коэффициенты сжатия (2,3,4 или 5):
K1 = 2
K2 = 5

s2 = signal.lfilter(np.array([1,1,1])/3, [1,-0.85], np.random.randn(250))

s31 = s2[0::2]
s32 = s2[0::5]
s33 = signal.decimate(s2, 2, ftype='fir')
s34 = signal.decimate(s2, 5, ftype='fir')

s41 = signal.resample_poly(s31, 2, 1)
s42 = signal.resample_poly(s32, 5, 1)
s43 = signal.resample_poly(s33, 2, 1)
s44 = signal.resample_poly(s34, 5, 1)

K1 = np.std(s2-s41)
K2 = np.std(s2-s42)
K3 = np.std(s2-s43)
K4 = np.std(s2-s44)
#
print(K1)
print(K2)
print(K3)
print(K4)