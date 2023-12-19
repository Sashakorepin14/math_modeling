import numpy as np
import matplotlib.pyplot as plt

def plot_ellipse(a = 0.5, b = 0.2):
    x = np.linspace(-1, 1, 100)
    y = np.linspace(-1, 1, 100)
    
    X, Y = np.meshgrid(x, y)
    
    elips = (X**2)/(a**2) + (Y**2)/(b**2) - 1
    plt.contour(x, y, elips, levels=[0])
    plt.xlabel('X')
    plt.ylabel('Y')
    plt.title('График эллипса')
    plt.axis('equal')
    
    plt.savefig('fig_task_3.png')
    
if __name__ == '__main__':
    plot_ellipse()