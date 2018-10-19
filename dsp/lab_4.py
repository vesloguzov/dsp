import math
import numpy as np
from scipy import signal
import matplotlib.pyplot as plt

N0 = 100

d_et = np.append([1], np.zeros(N0 - 1))  # эталонный сигнал

b_et = [1]
a_et = [1, 0.8]

z_et = signal.lfilter(b_et, a_et, d_et)

plt.plot(np.arange(N0), z_et, 'y', linewidth=1.0)
plt.plot(np.arange(N0), np.full((N0, 1), 0.05 * max(z_et)), 'r')
plt.plot(np.arange(N0), np.full((N0, 1), -0.05 * max(z_et)), 'r')


plt.show()
plt.close()

b_et = [1]
a4_et = [1, -0.8]
z_et = signal.lfilter(b_et, a4_et, d_et)
fz_et = np.abs(np.fft.fft(z_et))
plt.plot(np.arange(N0), fz_et, 'y', linewidth=1.0)
plt.plot(np.arange(N0), np.full((N0, 1), 0.707 * max(fz_et)), 'r')

plt.show()
plt.close()

f707 = [1 if x > 0.707*max(fz_et) else 0 for x in fz_et]
Fp = N0/2 - (np.where(np.flip(f707)[int(N0/2):] == 1)[0][0]+1) + 1
mz = [1 if x > 0.05*max(abs(z_et)) else 0 for x in abs(z_et)]
Dp = N0 - (np.where(np.flip(mz) == 1)[0][0]+1)


b_et = [1]
a_et = [1, -0.8]
K = 500

fz = 0
for i in np.arange(1, K + 1):
    x = np.random.randn(1000)
    z = abs(np.fft.fft(signal.lfilter(b_et, a_et, x)))
    fz = fz + np.array(z)
fz = fz/max(fz)
Noise = 1000
fz_et = abs(np.array(b_et)/np.array([(np.exp(1j * 2 * math.pi * x / Noise) * a_et[1] + 1) for x in np.arange(Noise)]))
fz_et = (np.array(fz_et) / max(fz_et))

fz_et_v = fz_et * 1.1
fz_et_u = fz_et * 0.9 * np.array([1 if x * 0.9 > 0 else 0 for x in fz_et])

plt.plot(np.arange(len(fz_et)), fz_et, 'y', linewidth=1.0)
plt.plot(np.arange(len(fz_et)), fz_et_v, 'b--')
plt.plot(np.arange(len(fz_et)), fz_et_u, 'b--')

plt.show()
plt.close()