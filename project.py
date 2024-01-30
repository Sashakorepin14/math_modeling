from matplotlib.animation import FuncAnimation
import matplotlib.pyplot as plt
import numpy as np
import random


def circle_move(time, R=0, x0=0, y0=0, vy0=0):

    x0 = x0
    y0 = y0 + vy0 * time
    alpha = np.arange(0, 3*np.pi, 0.1)
    r = R * time ** 1.1

    x = x0 + r*np.cos(alpha)
    y = y0 + r*np.sin(alpha)
    return x, y


	
def animate(i):
    for j in range(len(balls)):
        balls[j].set_data(circle_move(time=i, R=0.0005*r[j], x0=1*x[j], y0=0.01*y[j], vy0=0.01*vy[j]))


if __name__ == '__main__':
 
    fig, ax = plt.subplots()
    balls = []
    for i in range(100):
        ball, = plt.plot([], [], '-', color='b', label='Ball')
        balls.append(ball)
    
    r = []
    x = []
    y = []
    vy = []
    for j in range(len(balls)):
        r.append(random.randint(1, 99))
        x.append(random.randint(1, 99))
        y.append(random.randint(1, 99))
        vy.append(random.randint(1, 99))
    

    edge = 100
    plt.axis('equal')
    ax.set_xlim(0, edge)
    ax.set_ylim(0, edge)
    
    ani = FuncAnimation(fig,
                        animate,
                        frames=100,
                        interval=30
                       )
    	
    ani.save('project.gif') 