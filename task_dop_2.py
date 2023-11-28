import numpy as np

def fib():
    n = int(input())
    hz = np.zeros(n)
    a = 0
    b = 1
    hz[0] = a
    hz[1] = b
    for i in range(2, n):
        c = a + b
        hz[i] = c
        a = b
        b = c
    n -= 1
    return hz[n]
print(fib())