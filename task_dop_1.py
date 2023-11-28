import numpy as np

def stepen(a, n):
    b = 1
    for i in np.arange(n):
        b *= a
    return b
print(stepen(5, 5))
print(5**5)