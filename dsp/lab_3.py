import math
import numpy as np
from scipy import signal
import matplotlib.pyplot as plt

x = [1, 1, 1, 1, 1, -1, -1, 1, 1, -1, 1, -1, 1]
K = len(x)
N1 = 10
N0 = K * N1
# print("N0= ", N0)
x2 = np.matlib.repmat(x, N1, 1).flatten('F')
print(x2)

y_et = np.append(x2, np.zeros(N0 * 2))  # сигнал, который вводит студент

b_et = y_et[0:N0][::-1]  # фильтр, который вводит студент

S = int(np.floor(np.random.uniform(0, 1)*N0))

s_et = signal.lfilter(b_et, 1, y_et)

# print("S = ", S)
# print("len(y_et)= ", y_et)
y1_et = np.roll(np.roll(y_et, S), (1) * S)

ys1_et = y1_et + 0.5 * np.random.randn(1, 3 * N0)[0]

z = signal.lfilter(b_et, 1, ys1_et)

# plt.plot(ys1_et)
plt.plot(z)
plt.show()
plt.close()

# plt.plot(np.abs(np.fft.fft(ys1_et)))  # не будем делать
# plt.show()
# plt.close()
#
B_et = S   # случайный сдвиг
# print(B_et)
#
si = np.array(z).argmax(0) + 1
#
B_st = si - N0
# print("B_st = ", B_st)
#
# Ke_et = 1000
# v_et = np.zeros(50)
# for j in np.arange(1, 50 + 1):
#     pp = 2 * math.sqrt(N0)
#     q = 0
#     for i in np.arange(1, Ke_et + 1):
#         y2 = y_et + j / 25 * np.random.randn(1, 3 * N0)[0]
#         s2 = signal.lfilter(b_et, 1, y2)
#         w = (np.array(s2) > np.array(pp)).astype(int)
#         for x in np.arange(math.floor(N0-K/2)-1, math.floor(N0+K/2)+3):
#             w[x-1] = 0
#         q = q + np.double(sum(w) > 0)
#     v_et[j-1] = float(q/Ke_et)
#
# s_st = np.array(sorted((np.random.permutation(50)/25)[:10]))
#
# y2 = []
# s2 = []

s_st = np.array([0, 0.2, 0.4, 0.6, 0.8, 1.0, 1.2, 1.4, 1.6, 1.8])

Ku_j = 10
Ku_i = 10
v = [None]*10
print(K)
for j in np.arange(1, Ku_j + 1):
    pp = 2 * math.sqrt(N0)
    q = 0
    for i in np.arange(1, Ku_i + 1):
        y2 = y_et + s_st[j-1] * np.random.randn(1, 3 * N0)[0]
        s2 = signal.lfilter(b_et, 1, y2)  # выводим графики  y2 и s2
        if i == 1 and j == 1:
            plt.plot(s2)
            plt.plot(y2)
            plt.show()
            plt.close()
        w = (np.array(s2) > np.array(pp)).astype(int)
        for x in np.arange(math.floor(N0-K/2)-1, math.floor(N0+K/2)+3):
            w[x-1] = 0
        q = q + np.double(sum(w) > 0)
    if Ku_i == 10:
        v[j-1] = float(q/Ku_i)
print(v)


# Ku_j = 10
# Ku_i = 10
# v = [None]*10
# q = 0
#
# res_y2 = [[x for x in np.zeros(10)] for y in np.zeros(10)]
# res_s2 = [[x for x in np.zeros(10)] for y in np.zeros(10)]
#
# for j in np.arange(1, Ku_j + 1):
#     pp = 2 * math.sqrt(N0)
#     for i in np.arange(1, Ku_i + 1):
#         y2 = y_et + s_st[j-1] * np.random.randn(1, 3 * N0)[0]
#         s2 = signal.lfilter(b_et, 1, y2)  # выводим графики  y2 и s2
#         res_y2[j-1][i-1] = y2
#         res_s2[j-1][i-1] = s2
#         if j == 1 and i in [1,2,3]:
#             print(s2)
#         w = (np.array(s2) > np.array(pp)).astype(int)
#         for x in np.arange(math.floor(N0-K/2)-1, math.floor(N0+K/2)+3):
#             w[x-1] = 0
#         q = q + np.double(sum(w) > 0)
#     v[j-1] = float(q/Ku_i)
#     q = 0
# print(v)


