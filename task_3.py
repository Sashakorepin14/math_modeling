import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt

t = np.arange(-5, 5, 0.01)

def diff_func(z, t):
    y, omega = z
    dy_dt = omega
    domega_dt = np.sin(t) + np.cos(t)
        
    return dy_dt, domega_dt

y0 = 3
omega0 = 0

z0 = y0, omega0


sol = odeint(diff_func, z0, t)


plt.plot(t, sol[:, 1], 'b', label='omega(x)')


plt.savefig('task_3.png')