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

S = 6  # случайный сдвиг

y1_et = np.roll(np.roll(y_et, S), (-1) * S)

ys1_et = y1_et + 0.5 * np.random.randn(1, 3 * N0)[0]

z = signal.lfilter(b_et, 1, ys1_et)
# print(ys1_et)
plt.plot(ys1_et)
# print(max(z))
plt.plot(z)
plt.show()

plt.plot(np.abs(np.fft.fft(ys1_et)))
plt.show()

B_et = S

si = np.argmax(np.abs(z))
B_st = si - N0

# print(max(np.abs(z)))
# print(si)
