import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt

x = np.arange(-5, 5, 0.01)

def diff_func(a, x):
    y, z = a

    dy_dx = y**2 * z
    dz_dx = z/x - y * z**2
        
    return dy_dx, dy_dx

y0 = 1
z0 = -3

a0 = y0, z0


sol = odeint(diff_func, a0, x)


plt.plot(x, sol[:, 1], 'b', label='omega(x)')


plt.savefig('task_1.png')