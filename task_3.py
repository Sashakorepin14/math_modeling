import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

def butterfly_equations(t):
    x = 2 * np.cos(t) * (np.exp(np.cos(t)) - 2 * np.cos(4 * t) - np.sin(t/12)**5)
    y = 2 * np.sin(t) * (np.exp(np.cos(t)) - 2 * np.cos(4 * t) - np.sin(t/12)**5)
    return x, y

ax = plt.axes(xlim=(-10, 10), ylim=(-10, 10))