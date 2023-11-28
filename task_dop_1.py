import numpy as np

def stepen():
    a = float(input())
    n = float(input())
    for i in np.arange(n):
        a = a * a
    return a
print(stepen())