import numpy as np


def function():
    abcd = input()
    a = float(input())
    b = float(input())
    N = int(input())
    if abcd == 'y = x':
        x = np.linspace(a, b, N)
        y = x
    elif abcd == 'y = x**2':
        x = np.linspace(a, b, N)
        y = x**2
    elif abcd == 'y = k/x':
        k = float(input())
        x = np.linspace(a, b, N)
        y = k/x
    return y
print(function())