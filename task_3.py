import numpy as np

x0 = 0
v0x = 1
y0 = 0
v0y = 2
g = 9.8

t = np.arange(0, 5, 0.1)
x = x0 + v0x * t 
y = y0 + v0y - g * t**2 / 2

coords = np.zeros((len(t), 3))
for i in range(len(t)):
    coords[i, 0] = t[i]
    coords[i, 1] = x[i]
    coords[i, 2] = y[i]
print(coords)