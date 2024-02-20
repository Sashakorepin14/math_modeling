import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt

t = np.arange(-1, 1, 0.01)

def diff_func(z, t):
    x, y = z
    dx_dt = 3 * x - 2 * y + (2.718**(3*t)) / (2.718**t + 1)
    dy_dt = x - (2.718**(3*t)) / (2.718**t + 1)
        
    return dx_dt, dy_dt

x0 = 5
y0 = -7


z0 = x0, y0


sol = odeint(diff_func, z0, t)


plt.plot(t, sol[:, 1], 'b', label='omega(x)')


plt.savefig('task_2.png')