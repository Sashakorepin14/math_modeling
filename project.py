import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation


fig = plt.figure()
ax = plt.axes(xlim=(-100, 100), ylim=(-100, 100))
circle, = ax.plot([], [], '-')
plt.axis('equal')
 
def init():
    circle.set_data([], [])
    return circle,

def update(t):
    alpha = 0.5 
    phi = np.linspace(0, 2 * np.pi, 1000)
    R = alpha * t  
    x = R * np.cos(phi)
    for i in np.arange(-50, 50, 0.1):
        y = R * np.sin(phi) + i
    circle.set_data(x, y)
    return circle,

ani = FuncAnimation(fig, 
                    update,
                    frames=np.arange(0, 2*np.pi, 0.1),
                    interval=40
                    )
ani.save('project.gif')