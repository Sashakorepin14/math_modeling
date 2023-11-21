# Написать функцию, которая вычисляет среднее арифметическое элементов одномерного массива, переданного ей в качестве аргумента.

import numpy as np
a = np.zeros(5)
def sred_aref(a):   
    v = 0
    for i in range(len(a)):
        a[i] = int(input())
        v += a[i]
    return v/len(a)
print(sred_aref(a))

test_1 = np.arange(0, 100, 1)
sred_aref(test_1)