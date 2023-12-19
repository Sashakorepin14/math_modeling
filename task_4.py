import numpy as np
import matplotlib.pyplot as plt

def plot_logarithmic_spiral(b = 4):
    phi = np.linspace(0, 8*np.pi, 1000)
    r = np.exp**(b * phi)
    
    plt.polar(phi, r)
    plt.title('Логарифмическая спираль')
    plt.savefig('fig_task_4_1.png')

def plot_archimedean_spiral(k = 1):
    phi = np.linspace(0, 8*np.pi, 1000)
    r = k * phi
    
    plt.polar(phi, r)
    plt.title('Архимедова спираль')
    plt.savefig('fig_task_4_2.png')

def plot_staff_spiral(k = 2):
    phi = np.linspace(0.01, 8*np.pi, 1000)
    r = k / np.sqrt(phi)
    
    plt.polar(phi, r)
    plt.title('Спираль «жезл»')
    plt.savefig('fig_task_4_3.png')

def plot_polar_rose(k = 0.2):
    phi = np.linspace(0, 2*np.pi, 1000)
    r = np.sin(k * phi)
    
    plt.polar(phi, r)
    plt.title('Роза')
    plt.savefig('fig_task_4_4.png')
