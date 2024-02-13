import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt

t = np.arange(0, 12, 0.0001)

def investicii_func(n, t):
    dndt = - k * n * t
    return dndt

k = 0.08
n_0 = 1000

n_t = odeint(investicii_func, n_0, t)

plt.plot(t, n_t[:,0])
plt.savefig('3.png')