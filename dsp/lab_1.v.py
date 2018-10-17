import numpy as np
from scipy import signal
import matplotlib.pyplot as plt

N0 = 100

d = np.append([1, 1], np.zeros(N0 - 2))  # сигнал, вводимый студентом
d_et = np.append([1, 1], np.zeros(N0 - 2))  # эталонный сигнал

Ns = 5
b = np.ones(Ns)
b_et = np.ones(Ns)

z = signal.lfilter(b, 1, d)
z_et = signal.lfilter(b_et, 1, d_et)
fz_et = np.abs(np.fft.fft(z_et))

plt.stem(np.arange(N0), z, 'c', markersize=10)
plt.plot(np.arange(N0), z_et, 'y', linewidth=1.0)

plt.plot(np.arange(N0), np.full((N0, 1), 0.707 * max(z)), 'r', linewidth=1.0)
plt.show()
plt.close()
#
b = [1, -1, 1, -1, 1, -1, 1, -1,1]
b_et = np.ones(9)

w = np.hamming(9)
w_et = np.hamming(9)
#
z = signal.lfilter(b*w, 1, d)
print(w*b)

# z_et = signal.lfilter(w_et, 1, d_et)
#
# plt.plot(np.arange(N0), z_et)
# plt.plot(np.arange(N0), np.full((N0, 1), 0.707 * max(z)), 'r')
# plt.show()
# plt.close()
#
# fz_et = np.abs(np.fft.fft(z_et))
# mz = max(fz_et)
#
# plt.semilogy(fz_et)
# plt.show()
# plt.close()
#
# dz = np.diff(fz_et)
#
# dz_temp = np.multiply(dz[:-1], dz[1:])
# dz0 = [0 if d > 0 else 1 for d in dz_temp]
#
# mz1 = max(fz_et * np.append(dz0, np.zeros(len(fz_et) - len(dz0))))
#
# ubl_et = 20 * np.log10(mz1 / mz)
#
# print(ubl_et)
#
# K = 12.5
# i = 2
# kf = N0 / 2
#
# while kf > N0 / K:
#     f_et = np.abs(np.fft.fft(signal.lfilter(np.ones((i)), 1, d_et)))
#     z0 = [1 if d/max(f_et) < 0.707 else 0 for d in f_et]
#     kf = len(np.where(np.array(z0[:int(np.floor(len(z0)/2))]) < 1)[0]) + 1
#     i = i + 1
#
# p_et = i-1

# print(np.blackman(9))