import matplotlib.pyplot as plt
import numpy as np

def circle_plotter(r=15, a = 5, b = 2):

    x = np.arange(-2*r, 2*r, 0.1)
    y = np.arange(-2*r, 2*r, 0.1)

    X, Y = np.meshgrid(x, y)

    fxy = (x**2 / a**2) + (y**2 / b**2) = 1

    plt.contour(X, Y, fxy, levels=[0])
    plt.axis('equal')
    
    plt.savefig('fig_task_3.png')
    
if __name__ == '__main__':
	circle_plotter()