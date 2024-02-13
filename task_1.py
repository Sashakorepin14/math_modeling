import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt

t = np.arange(0, 100, 0.1)

def bacteriya_func(n, t):
    dndt = k * n
    return dndt

k = 0.05
n_0 = 1

n_t = odeint(bacteriya_func, n_0, t)

plt.plot(t, n_t[:,0])
plt.savefig('2.png')