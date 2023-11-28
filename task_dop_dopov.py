import numpy as np

def distance(x1, y1, x2, y2):
    if x1 > x2:
        x = x1 - x2
    else:
        x = x2 - x1

    if y1 > y2:
        y = y1 - y2
    else:
        y = y2 - y1

    d1 = x**2 + y**2
    d = np.sqrt(d1)
    return d
print(distance(0, 0, 1, 1))
    