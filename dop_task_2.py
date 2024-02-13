import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt

phi = np.linspace(0, np.pi, 100)
r = np.linspace(22.6, 28.2, 100)

def padenie_func(r, phi):
    dvdt =  r**2 * n * np.cos(phi)
    return dvdt

n = 1353

v_h = odeint(padenie_func, r, phi)

plt.plot(phi, v_h[:,0])
plt.savefig('6.png')