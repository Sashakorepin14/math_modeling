import matplotlib.pyplot as plt
import numpy as np
 
 
def cycloida(R = 3):
    t = np.arange(-2*np.pi, 2*np.pi, 0.1)
    
    x = R * (t - (np.sin(t)))
    y = R * (1 - (np.cos(t)))
    plt.plot(x, y, ls='-', lw=3)
    plt.axis('equal')
 
 
if __name__ == '__main__':
    cycloida()

def astroida(R = 3):
    t = np.arange(-2*np.pi, 2*np.pi, 0.1)
    
    x = R * (np.cos(t)**3)
    y = R * (np.sin(t)**3)
    plt.plot(x, y, ls='-', lw=3)
    plt.axis('equal')
    plt.savefig('fig_task_1_2.png')
 
 
if __name__ == '__main__':
    astroida()