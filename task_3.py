import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt

t = np.arange(0, 10, 0.1)

def padenie_func(v, t):
    dvdt = g - y * v**2
    return dvdt

y = 0.2
g = 9.8
v_0 = 0

v_t = odeint(padenie_func, v_0, t)

plt.plot(t, v_t[:,0])
plt.savefig('4.png')