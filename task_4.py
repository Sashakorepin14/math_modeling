import numpy as np
import matplotlib.pyplot as plt

def plot_logarithmic_spiral(b):
    c = np.linspace(0, 8*np.pi, 1000)
    r = 2.718 ** (b * c)
    
    plt.polar(c, r)
    plt.title('Логарифмическая спираль')
    plt.savefig('fig_task_4_1.png')

plot_logarithmic_spiral(0.1)

def plot_arhimedova_spiral(k):
    c = np.linspace(0, 8*np.pi, 1000)
    r = k * c

    plt.polar(c, r)
    plt.title('Архимедова спираль')
    plt.savefig('fig_task_4_2.png')

plot_arhimedova_spiral(2)

def plot_rod(k):
    c = np.linspace(0.01, 8*np.pi, 1000)
    r = k / (np.sqrt(c))

    plt.polar(c, r)
    plt.title('Жезл')
    plt.savefig('fig_task_4_3.png')

plot_rod(1)

def plot_rose(k):
    c = np.linspace(0.01, 8*np.pi, 1000)
    r = np.sin(k * c)

    plt.polar(c, r)
    plt.title('Роза')
    plt.savefig('fig_task_4_4.png')

plot_rose(10)