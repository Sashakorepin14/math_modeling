import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation


fig = plt.figure()
ax = plt.axes(xlim=(-10, 10), ylim=(-10, 10))
circle, = ax.plot([], [], 'o')
plt.axis('equal')

def init():
    circle.set_data([], [])
    return circle,

def update(t):
    alpha = 2.0  
    phi = np.linspace(0, 2 * np.pi, 1000)  
    radius = alpha * t  
    x = radius * np.cos(phi)  
    y = radius * np.sin(phi)  
    circle.set_data(x, y)
    return circle,

ani = FuncAnimation(fig, 
                    update,
                    frames=np.arange(0, 2*np.pi, 0.1),
                    interval=40
                    )
ani.save('animation.3.gif')