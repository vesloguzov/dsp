import math
import numpy as np
from scipy import signal
import matplotlib.pyplot as plt

N0 = 100

d_et = np.append([1], np.zeros(N0 - 1))  # эталонный сигнал

b_et = [1]
a_et = [1, 0.8]

z_et = signal.lfilter(b_et, a_et, d_et)
#
# plt.plot(np.arange(N0), z_et, 'y', linewidth=1.0)
# plt.plot(np.arange(N0), np.full((N0, 1), 0.05 * max(z_et)), 'r')
# plt.plot(np.arange(N0), np.full((N0, 1), -0.05 * max(z_et)), 'r')

a4_et = [1, -0.8]
z_et = signal.lfilter(b_et, a4_et, d_et)
fz_et = np.abs(np.fft.fft(z_et))
# plt.plot(np.arange(N0), fz_et, 'y', linewidth=1.0)
# plt.plot(np.arange(N0), np.full((N0, 1), 0.707 * max(fz_et)), 'r')

F_st = 4

f707 = [1 if x > 0.707*max(fz_et) else 0 for x in fz_et]
Fp = N0/2 - (np.where(np.flip(f707)[int(N0/2):] == 1)[0][0]+1) + 1

Dp_st = 13

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

N3 = 1000

fz_et = abs(np.array(b_et)/np.array([(np.exp(1j * 2 * math.pi * x / N3) * a_et[1] + 1) for x in np.arange(N3)]))
fz_et = (np.array(fz_et) / max(fz_et))

fz_et_v = fz_et * 1.1
fz_et_u = fz_et * 0.9  # Тут дописать, но, возможно, оно работоспособно


plt.plot(np.arange(len(fz_et)), fz_et, 'y', linewidth=1.0)
plt.plot(np.arange(len(fz_et)), fz_et_v, 'b--')
plt.plot(np.arange(len(fz_et)), fz_et_u, 'b--')

# print()

plt.show()
plt.close()

# print(np.arange(N0))
# plt.stem(np.arange(N0), z, 'c', markersize=10)
# plt.plot(np.arange(N0), z_et, 'y', linewidth=1.0)
#
# plt.plot(np.arange(N0), np.full((N0, 1), 0.707 * max(z)), 'r', linewidth=1.0)
# plt.show()
# plt.close()
# #
# b = [1, -1, 1, -1, 1, -1, 1, -1,1]
# b_et = np.ones(9)
#
# w = np.hamming(9)
# w_et = np.hamming(9)
# z = signal.lfilter(b*w, 1, d)

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