import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

frames = 500
seconds_in_year = 365 * 25 * 60 * 60
years = 2
t = np.linspace(0, 100, frames)

def move_func(s, t):
    r, v_r, phi = s

    drdt = v_r
    dv_rdt = - 1/(2*r)**2 + l**2/r**3 - 3*(l**2/r**4)
    dphidt = l/r**2
    
    return drdt, dv_rdt, dphidt


G = 6.67 * 10**(-11)
M = 1.998 * 10**30
l = 1.3 * np.sqrt(20 / 2)

r0 = 20
v_r0 = 0
phi0 = 0
s0 = (r0, v_r0, phi0)

sol = odeint(move_func, s0, t)

def solve_func(i, key):
    if key == 'point':
        x = sol[i, 0]
        y = sol[i, 2]
    else:
        x = sol[:i, 0]
        y = sol[:i, 2]
    return x, y
fig, ax = plt.subplots()
ball, = plt.plot([], [], 'o', color='b')
ball_line, = plt.plot([], [], '-', color='b')
plt.plot([0], [0], 'o', color='y', ms = 20)
def animate(i):
    ball.set_data(solve_func(i, 'point'))
    ball_line.set_data(solve_func(i, 'line'))
ani = FuncAnimation(fig, animate, frames=frames, interval=30)
plt.axis('equal')
edge = 5 * 149*10**6
ax.set_xlim(-edge, edge)
ax.set_ylim(-edge, edge)
ani.save('earth_sun.gif')