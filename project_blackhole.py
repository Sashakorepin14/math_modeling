import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation


def move_func(s, t):
    r, v_r, phi = s

    drdt = v_r
    dv_rdt = - r_g * c**2 /(2*r**2) + l**2/r**3 - 1.5*l**2/r**4
    dphidt = l/r**2
    
    return drdt, dv_rdt, dphidt

Msun = 1.9891e30
G = 6.67e-11
M = Msun * 3.75e6
c = 3e8
r_g = 2*G*M/c**2

ae = 149e9
r0 = 120 * ae
v_r0 = 0
phi0 = 0

v_phi0 = c * 0.02
l = v_phi0 * r0
time = 365 * 24 * 3600

N = 3000
t = np.linspace(0, time*10, N)
s0 = (r0, v_r0, phi0)
sol = odeint(move_func, s0, t)

def solve_func(i, key):
    if key == 'point':
        r = sol[i, 0]
        phi = sol[i, 2]

        x = r * np.cos(phi)
        y = r * np.sin(phi)
    else:
        r = sol[:i, 0]
        phi = sol[:i, 2]

        x = r * np.cos(phi)
        y = r * np.sin(phi)
    return x, y

fig, ax = plt.subplots()

ball, = plt.plot([], [], 'o', color='y')
ball_line, = plt.plot([], [], '-', color='y')
plt.plot([0], [0], 'o', color='0', ms = 20)


def animate(i):
    ball.set_data(solve_func(i, 'point'))
    ball_line.set_data(solve_func(i, 'line'))

ani = FuncAnimation(fig, animate, frames=N, interval=30)

plt.axis('equal')
edge = 2 * r0
ax.set_xlim(-edge, edge)
ax.set_ylim(-edge, edge)

ani.save('project2.gif')