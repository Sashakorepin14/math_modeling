from matplotlib.animation import FuncAnimation
import matplotlib.pyplot as plt
import numpy as np


def babichka_(t):
    x = np.sin(t)*(2.718**np.cos(t) - 2*np.cos(4*t) + np.sin(t/12)**5)
    y = np.cos(t)*(2.718**np.cos(t) - 2*np.cos(4*t) + np.sin(t/12)**5)
    return x, y

x, y = [], []
def animate(t):
    coords = babichka_(t)
    x.append(coords[0])
    y.append(coords[1])

    babichka.set_data(x, y)


if __name__ == '__main__':

    fig, ax = plt.subplots()
    babichka, = plt.plot([], [], '-', color='b', label='babichka')

    edge = 10
    plt.axis('equal')
    ax.set_xlim(-edge, edge)
    ax.set_ylim(-edge, edge)

    ani = FuncAnimation(fig,
                        animate,
                        frames=np.arange(0, 12*np.pi, 0.1),
                        interval=30)

    ani.save('task3Lab7.gif') 



def serdce_(t):
    x = 16*np.sin(t)**3
    y = 13*np.cos(t) - 5*np.cos(2*t) - 2*np.cos(3*t) - np.cos(4*t)
    return x, y

x, y = [], []
def animate(t):
    coord = serdce_(t)
    x.append(coord[0])
    y.append(coord[1])

    serdce.set_data(x, y)


if __name__ == '__main__':

    fig, ax = plt.subplots()
    serdce, = plt.plot([], [], '-', color='r', label='Ball')

    edge = 50
    plt.axis('equal')
    ax.set_xlim(-edge, edge)
    ax.set_ylim(-edge, edge)

    ani = FuncAnimation(fig,
                        animate,
                        frames=np.arange(0, 2*np.pi, 0.01),
                        interval=30)

    ani.save('task3.1Lab7.gif')