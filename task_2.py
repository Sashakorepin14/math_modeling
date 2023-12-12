import matplotlib.pyplot as plt
import numpy as np


def giperbola(k=2):
    x = np.arange(0.5, 5, 0.01)
    x1 = np.arange(-5, -0.5, 0.01)
    y = k/x
    y1 = k/x1

    plt.plot(x, y, label='my giperbola')
    plt.plot(x1, y1, label='my giperbola')
    plt.xlabel('coord - x')
    plt.ylabel('coord - y')
    plt.axis('equal')
    plt.savefig('fig_task_2.jpg')

if __name__ == '__main__':
	giperbola()