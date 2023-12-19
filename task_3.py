import numpy as np
import matplotlib.pyplot as plt

def ellipse(N, a = 0.5, b = 0.2):
    x = np.linspace(-1, 1, N)
    y = np.linspace(-1, 1, N)
    elips = (X**2)/(a**2) + (Y**2)/(b**2) - 1
    
    X, Y = np.meshgrid(x, y)
    plt.contour(x, y, elips, levels=[0])
    plt.xlabel('X')
    plt.ylabel('Y')
    plt.title('График эллипса')
    plt.axis('equal')
    plt.grid(True)
    
    plt.savefig('fig_task_3.png')
    
if __name__ == '__main__':
    ellipse(100)