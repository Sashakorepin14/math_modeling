import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation


def butterfly(t):
    x = (np.sin(t)* (2,718 ** (np.cos(t)) - 2 * np.cos(4 * t) + (np.sin(t/12) ** 5))) 
    y = (np.cos(t)* (2,718 ** (np.cos(t)) - 2 * np.cos(4 * t) + (np.sin(t/12) ** 5))) 
    return x, y


if __name__ == '__main__':
 
    fig, ax = plt.subplots()
    hz, = ax.plot([], [], '-', color='r')
 
    plt.axis('equal')
    ax.set_xlim(-25, 25)
    ax.set_ylim(-25, 25)

    def update(frame):
        t =  frame * 0.1
        x, y = butterfly(t) 
        hz.set_data(x, y)
        return hz,

    
    ani = FuncAnimation(fig,
                        update,
                        frames=100,
                        interval=30
                       )
    
	
    ani.save('animation_4.gif') 