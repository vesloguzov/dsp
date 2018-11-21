import math
import random
import string
import numpy as np
from scipy import signal
import matplotlib.pyplot as plt

N0 = 1000
rand_1 = 0.82038
rand_2 = 0.413
rand_3 = 0.04766

f0 = 200 + np.floor(250 * rand_1)
fm = np.floor(50*rand_2)
m = 0.2 + 0.8*rand_3

d1 = (1 + m * np.cos(2*math.pi*fm*np.arange(0, N0)/N0)) * (np.cos(2 * math.pi * f0 * np.arange(0, N0) / N0))

# print(f0)
# print(fm)
# print(m)

plt.plot(np.arange(0, N0), d1)
plt.show()
plt.close()
plt.stem(np.arange(0, N0), np.abs(np.fft.fft(d1)))
plt.show()
plt.close()

rand_4 = [0.33308, 0.81950, 0.68199, 0.52076, 0.90551, 0.28840, 0.63247, 0.11402, 0.88244, 0.82465]
rand_5 = 0.28217
rand_6 = 0.78565

code = (np.array(rand_4) > 0.5).astype(int)
f0 = 5 + np.floor(5*rand_5)
Ne = 1 + np.floor(9*rand_6)

N1 = 4 * f0 * Ne
S1 = np.matlib.repmat(code, np.int(N1), 1).flatten('F')

Smf = (S1 * np.cos(2*math.pi*f0*np.arange(0, 10*N1)/N1)) + ((1 - S1) * np.cos(4*math.pi*f0*np.arange(0, 10*N1)/N1))

Smp = (2*(S1-0.5)) * np.cos(2*math.pi*f0*np.arange(0, 10*N1)/N1)
plt.plot(Smp)
plt.show()
plt.close()

# print(Smp)

soob = ''.join([s for s in random.sample(string.ascii_uppercase, 5)])
# soob = 'KWHGV'
code = ''.join("0"+format(ord(x), 'b') for x in soob)  # разобраться с ноликом в начале
LS = len(soob)
L = len(code)

rand_7 = 0.45263
rand_8 = 0.87775

f0 = 5 + np.floor(5 * rand_7)
Ne = 1 + np.floor(9 * rand_8)

N1 = int(4 * f0 * Ne)

S1 = (np.matlib.repmat(np.array([ord(x) for x in code]), np.int(N1), 1) - 48).flatten('F')

S1p = (2 * (S1-0.5)) * np.cos(2 * math.pi * f0 * np.arange(0, L*N1)/N1) + (0.5 * np.random.randn(np.int(N1*L)))

S10 = np.cos(2 * math.pi * f0 * np.arange(0, L*N1)/N1)

SD = S1p * S10

plt.plot(np.arange(0, N1*8), S1p[0:np.int(N1*8)])
plt.show()
plt.close()
plt.plot(np.arange(0, N1*8), SD[0:np.int(N1*8)])
plt.show()
plt.close()

b_st = np.array([1, 1, 1, 1, 1, 1, 1, 1]) / 3
a_st = np.array([1, -0.9])

z = signal.lfilter(b_st, a_st, SD)

plt.plot(np.arange(0, np.int(N1*8)), z[0:np.int(N1*8)])
plt.stem(np.arange(N1/2, N1*8, N1), np.take(z, np.arange(np.int(N1/2), np.int(N1*8), np.int(N1))), 'r')
plt.show()
plt.close()

dsig = (np.take(z, np.arange(np.int(N1/2), len(z), np.int(N1))) > 0).astype(int)
csig = ''.join([str(e) for e in dsig])
vs = [None]*LS
vs_str = ''
for i in np.arange(LS):
    q = csig[i*8:(i+1)*8]
    q_str = chr(int(q, 2))
    vs[i] = q_str
    vs_str = vs_str + q_str
print(vs)
print(vs_str)