import matplotlib.pyplot as plt
import numpy as np
from matplotlib.animation import FuncAnimation

	
fig, ax = plt.subplots()

fig, ax = plt.subplots()
xdata, ydata = [], []

ax.set_xlim(0, 2*np.pi)
ax.set_ylim(-1, 1)

def update(frame):
    xdata.append(frame)
    ydata.append(np.sin(frame))
    anim_object.set_data(xdata, ydata)
    return anim_object,

ani = FuncAnimation(fig, 
                    update,
                    frames=np.arange(0, 2*np.pi, 0.1),
                    interval=40
                    )

ani.save('animation.1.gif')