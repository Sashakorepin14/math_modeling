import numpy as np
import random

def hz(N):
    a = np.zeros(N)
    b = np.zeros(N)
    c = np.zeros(N)
    for i in range(N):
        a[i] = random.randint(0, 100)
        b[i] = random.randint(0, 100)
        c[i] = random.randint(0, 100)
    max1 = np.max(a)
    max2 = np.max(b)
    max3 = np.max(c)
    sum1 = sum(a)
    sum2 = sum(b)
    sum3 = sum(c)
    return max1, max2, max3, sum1, sum2, sum3
print(hz(5))