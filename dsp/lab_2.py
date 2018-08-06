import numpy as np
import math
from scipy import signal
import matplotlib.pyplot as plt

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
d8_et = [math.exp((-1)*alpha*x) for x in np.arange(N8)]

print(d8_et)
# d3_et=cos(math.pi*(0:N3-1)/2)
