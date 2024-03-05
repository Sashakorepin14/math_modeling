import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

frames = 200
seconds_in_year = 365 * 25 * 60 * 60
years = 1
t = np.linspace(0, years*seconds_in_year, frames)

def move_func(s, t):
    (x1, v_x1, y1, v_y1,
     x2, v_x2, y2, v_y2,
     x3, v_x3, y3, v_y3,
     x4, v_x4, y4, v_y4) = s

    dxdt1 = v_x1
    dvxdt1 = -G * M *x1 / (x1**2 + y1**2)**1.5
    dydt1 = v_y1
    dvydt1 = -G * M *y1 / (x1**2 + y1**2)**1.5
    
    dxdt2 = v_x2
    dvxdt2 = -G * M *x2 / (x2**2 + y2**2)**1.5
    dydt2 = v_y2
    dvydt2 = -G * M *y2 / (x2**2 + y2**2)**1.5

    dxdt3 = v_x3
    dvxdt3 = -G * M *x3 / (x3**2 + y3**2)**1.5
    dydt3 = v_y3
    dvydt3 = -G * M *y3 / (x3**2 + y3**2)**1.5

    dxdt4 = v_x4
    dvxdt4 = -G * M *x4 / (x4**2 + y4**2)**1.5
    dydt4 = v_y4
    dvydt4 = -G * M *y4 / (x4**2 + y4**2)**1.5

    return (dxdt1, dvxdt1, dydt1, dvydt1,
            dxdt2, dvxdt2, dydt2, dvydt2,
            dxdt3, dvxdt3, dydt3, dvydt3,
            dxdt4, dvxdt4, dydt4, dvydt4)

G = 6.67 * 10**(-11)
M = 1.998 * 10**30
# Земля
x10 = 149 * 10**9
v_x10 = 0
y10 = 0
v_y10 = 30000
# Меркурий
x20 = 0
v_x20 = -47360
y20 = 0.387 * 149 * 10**9
v_y20 = 0
# Венера
x30 = - 0.723 * 149 * 10**9
v_x30 = 0
y30 = 0
v_y30 = 35020
# Марс
x40 = 0
v_x40 = - 5030
y40 = 1.52 * 149 * 10**9
v_y40 = 0

s0 = (x10, v_x10, y10, v_y10,
      x20, v_x20, y20, v_y20,
      x30, v_x30, y30, v_y30,
      x40, v_x40, y40, v_y40)

sol = odeint(move_func, s0, t)


def solve_func(i, key):
    if key == 'point':
        x1 = sol[i, 0]
        y1 = sol[i, 2]
        x2 = sol[i, 4]
        y2 = sol[i, 6]
        x3 = sol[i, 8]
        y3 = sol[i, 10]
        x4 = sol[i, 12]
        y4 = sol[i, 14]
    else:
        x1 = sol[:i, 0]
        y1 = sol[:i, 2]
        x2 = sol[:i, 4]
        y2 = sol[:i, 6]
        x3 = sol[:i, 8]
        y3 = sol[:i, 10]
        x4 = sol[:i, 12]
        y4 = sol[:i, 14]
    return ((x1, y1),(x2,y2),(x3,y3),(x4,y4))
    
fig, ax = plt.subplots()

ball1, = plt.plot([], [], 'o', color='b')
ball_line1, = plt.plot([], [], '-', color='b')

ball2, = plt.plot([], [], 'o', color='b')
ball_line2, = plt.plot([], [], '-', color='b')

ball3, = plt.plot([], [], 'o', color='g')
ball_line3, = plt.plot([], [], '-', color='g')

ball4, = plt.plot([], [], 'o', color='r')
ball_line4, = plt.plot([], [], '-', color='r')

plt.plot([0], [0], 'o', color='y', ms = 20)


def animate(i):
    ball1.set_data(solve_func(i, 'point')[0])
    ball_line1.set_data(solve_func(i, 'line')[0])

    ball2.set_data(solve_func(i, 'point')[1])
    ball_line2.set_data(solve_func(i, 'line')[1])

    ball3.set_data(solve_func(i, 'point')[2])
    ball_line3.set_data(solve_func(i, 'line')[2])

    ball4.set_data(solve_func(i, 'point')[3])
    ball_line4.set_data(solve_func(i, 'line')[3])

ani = FuncAnimation(fig, animate, frames=frames, interval=30)

plt.axis('equal')
edge = 4 * x10
ax.set_xlim(-edge, edge)
ax.set_ylim(-edge, edge)

ani.save('task_1.gif')