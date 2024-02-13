import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt

h = np.arange(0, 100, 1)

def padenie_func(v, h):
    dvdt =  g - (y * v**3)/m
    return dvdt

m = 10000
y = 0.2
g = 9.8
v_0 = 0

v_h = odeint(padenie_func, v_0, h)

plt.plot(h, v_h[:,0])
plt.savefig('5.png')