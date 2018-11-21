import json
import random
import math
import numpy as np
from scipy import signal
import matplotlib.pyplot as plt


x = [1, 1, 1, 1, 1, -1, -1, 1, 1, -1, 1, -1, 1]
K = len(x)
N1 = 10
N0 = K * N1
x2 = np.array([[1, 1, 1, 1, 1, -1, -1, 1, 1, -1, 1, -1, 1],
             [1, 1, 1, 1, 1, -1, -1, 1, 1, -1, 1, -1, 1],
             [1, 1, 1, 1, 1, -1, -1, 1, 1, -1, 1, -1, 1],
             [1, 1, 1, 1, 1, -1, -1, 1, 1, -1, 1, -1, 1],
             [1, 1, 1, 1, 1, -1, -1, 1, 1, -1, 1, -1, 1],
             [1, 1, 1, 1, 1, -1, -1, 1, 1, -1, 1, -1, 1],
             [1, 1, 1, 1, 1, -1, -1, 1, 1, -1, 1, -1, 1],
             [1, 1, 1, 1, 1, -1, -1, 1, 1, -1, 1, -1, 1],
             [1, 1, 1, 1, 1, -1, -1, 1, 1, -1, 1, -1, 1],
             [1, 1, 1, 1, 1, -1, -1, 1, 1, -1, 1, -1, 1]])

y_et = np.append(x2.flatten('F'), np.zeros(N0 * 2))  # сигнал, который вводит студент
b_et = y_et[0:N0][::-1]  # фильтр, который вводит студент

# print(len(y_et))
# print(len(b_et))

student_data = dict()
student_data["y"] = y_et
student_data["b"] = b_et
student_data["Ku_j"] = 9  # от 1 до 10
student_data["Ku_i"] = 8  # от 1 до 10


def get_graphic(student_data):
    y2 = []
    s2 = []
    y = np.array(student_data["y"])
    b = np.array(student_data["b"])
    N0 = len(b)

    s_st = np.array([0, 0.2, 0.4, 0.6, 0.8, 1.0, 1.2, 1.4, 1.6, 1.8])

    Ku_j = int(student_data["Ku_j"])
    Ku_i = int(student_data["Ku_i"])
    v = np.zeros(10)
    for j in np.arange(1, Ku_j + 1):
        # pp = 2 * math.sqrt(N0)
        # q = 0
        for i in np.arange(1, Ku_i + 1):
            y2 = y + s_st[j-1] * np.random.randn(1, 3 * N0)[0]
            s2 = signal.lfilter(b, 1, y2)  # выводим графики  y2 и s2

            print(len(s2))

    # plt.plot(y2)
    # plt.plot(s2)
    # plt.plot(np.arange(len(y)), np.full((len(y), 1), 0.707 * max(s2)), 'r')
    #
    # plt.show()
    # plt.close()

# get_graphic(student_data)

print()

# Ku_j = 3
#
#
# for j in np.arange(1, Ku_j + 1):
#     print(j)