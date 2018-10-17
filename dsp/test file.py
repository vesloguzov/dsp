import json
import random
import math
import numpy as np

lol = '{"student_signal":[2,2,2,2,2],"student_filter":[1,1,1,1,1,1],"a":"2","student_window":"hamming"}'


# print("LOL")
# print(json.loads(lol)['a'])
#
# filter_windows = [
#     {
#         "name": "hamming",
#         "title": "окно Хэмминга"
#     },
#     {
#         "name": "blackman",
#         "title": "окно Блэкмана"
#     },
#     {
#         "name": "rectangular",
#         "title": "прямоугольное окно"
#     }
# ]
# filter_type = random.choice([
#     {
#         "name": "filter type name example",
#         "title": "filter type title example",
#                  "window":[x for x in filter_windows if x["name"] == "hamming"][0]
# }
# ])

# def arrays_is_equal(x, y):
#     return a == y
#
#
# def numbers_is_equal(x, y, tol=0.5, rel=0.00005):
#     if tol is rel is None:
#         raise TypeError('cannot specify both absolute and relative errors are None')
#     tests = []
#     if tol is not None: tests.append(tol)
#     if rel is not None: tests.append(rel * abs(x))
#     assert tests
#     return abs(x - y) <= max(tests)
# N0 = 100
# lol = '[{"id":"kekid"}, {"id": "idlol"}]'
# # print([x['id'] for x in json.loads(lol)])
# lol = json.loads(lol)
# lol.append({"id":"234r23r"})
# print(len(json.dumps(lol)))

# N0 = 101
# Q = 15

# Ns = 5
# tmp = math.ceil(Ns / 2)
# filter = np.tile([1, -1], tmp)[0:Ns]
# tmp1 = math.ceil(math.ceil(N0/Q)/2)
# tmp1 = np.tile([1, -1], tmp)[0:Ns]
# signal = np.append(tmp2, np.zeros(N0 - len(tmp2)))
print(int(float(3.5)))


