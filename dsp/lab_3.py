import math
import numpy as np
from scipy import signal
import matplotlib.pyplot as plt

x = [1, 1, 1, 1, 1, -1, -1, 1, 1, -1, 1, -1, 1]
K = len(x)
N1 = 10
N0 = K * N1

x2 = np.matlib.repmat(x, N1, 1)
y_et = np.append(x2.flatten('F'), np.zeros(N0 * 2))

b_et = y_et[0:N0][::-1]

s_et = signal.lfilter(b_et, 1, y_et)

S = int(np.floor(np.random.uniform(0, 1)*N0))  # случайный сдвиг
y1_et = np.roll(np.roll(y_et, S), (-1) * S)

ys1_et = y1_et + 0.5 * np.random.randn(1, 3 * N0)[0]
z = signal.lfilter(b_et, 1, ys1_et)

plt.plot(ys1_et)
plt.plot(z)
plt.show()
plt.close()

plt.plot(np.abs(np.fft.fft(ys1_et)))
plt.show()
plt.close()

B_et = S
si = np.array(z).argmax(0) + 1

B_st = si - N0  # Вот тут правильно ли?

Ke_et = 1000
v_et = np.zeros(50)
for j in np.arange(1, 50 + 1):
    pp = 2 * math.sqrt(N0)
    q = 0
    for i in np.arange(1, Ke_et + 1):
        y2 = y_et + j / 25 * np.random.randn(1, 3 * N0)[0]
        s2 = signal.lfilter(b_et, 1, y2)
        w = (np.array(s2) > np.array(pp)).astype(int)
        for x in np.arange(math.floor(N0-K/2)-1, math.floor(N0+K/2)+3):
            w[x-1] = 0
        q = q + np.double(sum(w) > 0)
    v_et[j-1] = float(q/Ke_et)

s_st = np.array(sorted((np.random.permutation(50)/25)[:10]))

Ku = 25
v = np.zeros(10)
for j in np.arange(1, 10 + 1):
    pp = 2 * math.sqrt(N0)
    q = 0
    for i in np.arange(1, Ku + 1):
        y2 = y_et + s_st[j-1] * np.random.randn(1, 3 * N0)[0]
        s2 = signal.lfilter(b_et, 1, y2)
        w = (np.array(s2) > np.array(pp)).astype(int)
        for x in np.arange(math.floor(N0-K/2)-1, math.floor(N0+K/2)+3):
            w[x-1] = 0
        q = q + np.double(sum(w) > 0)
    v[j-1] = float(q/Ku)


plt.stem(np.arange(1, 51)/25, v_et, 'c')

(markers, stemlines, baseline) = plt.stem(s_st, v, 'y')
plt.setp(markers, marker='D', markersize=10, markeredgecolor="orange", markeredgewidth=2)

plt.show()
plt.close()

print('end')

