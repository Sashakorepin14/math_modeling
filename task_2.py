import numpy as np
from task_1 import acceleration_of_gravity as g
from task_1 import planka_constant as h1
from task_1 import bolcman_constant as k
from task_1 import e
h = 100 
a = np.pi / 3
b = 30

m = g * h * np.tan(b)**2
n = 2 * np.cos(a)**2 * (1 - np.tan(b) * np.tan(a))
v = np.sqrt(m / n)
print(v)



T = 200
e = 300

N = (2/np.sqrt(np.pi)) * (h1 / (k*T)**(3/2)) * e**((e*-1)/ k*T) * e**(T/2)
print(N)