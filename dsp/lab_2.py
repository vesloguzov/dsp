import numpy as np
import math
from scipy import signal
import matplotlib.pyplot as plt, mpld3
from utils import save_stem

# дискретная дельта-функция
N1 = 100
d1 = np.append([1], np.zeros(N1 - 1))
d1_et = np.append([1], np.zeros(N1 - 1))

# гармоничекое колебание fd/4
N3 = 100
d3_et = [math.cos(math.pi * x / 2) for x in np.arange(N3)]

# гармоничекое колебание fd/2
N4 = 100
d3_et = [math.cos(math.pi * x) for x in np.arange(N4)]

# экспоненциальный видеоимпульс
N8 = 100
alpha = 2
d8_et = [math.exp((-1) * alpha * x) for x in np.arange(N8)]

N9 = 100
alpha = 2
d9_et = np.multiply([math.pow((-1), y) for y in np.arange(N9)], [math.exp((-1) * alpha * x) for x in np.arange(N9)])



K = 4
d3 = [math.cos((math.pi * x) / 2) for x in np.arange(N3)]
sp = np.abs(np.fft.fft(d3))
save_stem(N3, sp, "gr_1.html")
# plt.stem(np.arange(N3), sp)
# plt.show()


ns_et = [N1 / K, N1 - N1 / K]
ns = [25, 75]

rand_number = 0.53413  # round(np.random.uniform(0,1,1)[0], 5)
K = (N1 / 2 - 1) * rand_number

d3_et = [np.exp(2j * math.pi * K * x / N3) for x in np.arange(N3)]
d3 = [np.exp(2j * math.pi * K * x / N3) for x in np.arange(N3)]

sp = np.abs(np.fft.fft(d3))
save_stem(N3, sp, "gr_2.html")
# plt.stem(np.arange(N3), sp)
# plt.show()
# mpld3.save_html(fig, 'interactive_fig_1.html')

K_st = 24.79

rand_number_1 = 0.048535  # round(np.random.uniform(0,1,1)[0], 5)
Nk = 2 + math.floor(8 * rand_number_1)

rand_array = [2.0103, 42.3491]  # [50*x for x in np.random.uniform(0, 1, Nk)]
f = np.sort([50 * x for x in [2.0103, 42.3491]])
df = np.diff(f)
# !!!!!!! MATLAB: f(df<3)=[];
Nk0 = len(f)
print(Nk0)
d9 = np.zeros(N3)

for i in np.arange(1, Nk0 + 1):
    d9 = np.array(d9) + np.array([math.cos(2 * math.pi * f[i - 1] * x / N3) for x in np.arange(N3)])

sp = np.abs(np.fft.fft(d9))
save_stem(N3, sp, "gr_3.html")
# plt.stem(np.arange(N3), sp)
# plt.show()

# f_st=[16 35 38 45]; -- это откуда?
