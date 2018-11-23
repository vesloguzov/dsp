import json
import random
import math
import numpy as np
import scipy as signal
import matplotlib.pyplot as plt


# Ku_j = 0
# number = [0.89978684, 0.90863665,  0.9362055, 0.98585497, 1.06437791, 1.18459886, 1.37164948, 1.68007446, 2.251535, 3.59758502, 10.02510877, 11.61880921, 3.6607721, 2.20823996, 1.62901037, 1.34575158, 1.20866821, 1.16725961, 1.20866821, 1.34575158, 1.62901037, 2.20823996, 3.6607721, 11.61880921, 10.02510877, 3.59758502, 2.251535, 1.68007446, 1.37164948, 1.18459886, 1.06437791, 0.98585497, 0.9362055, 0.90863665]
# last_numeral = float(str(number)[-1])
# for i, j in enumerate(number):
#     if j == 11.61880921:
#         print(i)
# print(np.argmax(number))

def values_count_in_array(x, value=None):
    return len(np.where(np.array(x) == value)[0])

def numbers_is_equal(x, y, tolerance=0.5, rel=0.00005):
    if tolerance is rel is None:
        raise TypeError('cannot specify both absolute and relative errors are None')
    tests = []
    if tolerance is not None: tests.append(tolerance)
    if rel is not None: tests.append(rel * abs(x))
    assert tests
    return abs(x - y) <= max(tests)

def arrays_is_equal_by_elements(x, y, tolerance=0.01):
    res = []
    if len(x) != len(y):
        raise TypeError('arrays must be equal length')
    for idx, x_el in enumerate(x):
        res.append(numbers_is_equal(x[idx], y[idx], tolerance=tolerance))
    return res

print(np.random.rand())