import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Устанавливаем параметры анимации
fig = plt.figure()
ax = plt.axes(xlim=(-10, 10), ylim=(-10, 10))
circle, = ax.plot([], [], 'bo')

# Функция для инициализации анимации
def init():
    circle.set_data([], [])
    return circle,

# Функция для обновления данных на каждом кадре анимации
def update(t):
    alpha = 2.0  # Параметр, определяющий скорость расширения радиуса
    phi = np.linspace(0, 2 * np.pi, 100)  # Значения параметра φ от 0 до 2π
    radius = alpha * t  # Расчет радиуса круга в момент времени t
    x = radius * np.cos(phi)  # Вычисление координаты x
    y = radius * np.sin(phi)  # Вычисление координаты y
    circle.set_data(x, y)
    return circle,

ani = animation(fig, 
                update,
                frames=np.arange(0, 2*np.pi, 0.1),
                interval=40
                )

ani.save('animation.1.gif')