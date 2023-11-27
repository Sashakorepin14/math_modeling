# Создайте функцию, которая перемножает все элементы входного одномерного массива, подающегося на вход в качестве аргумента (массив должен быть целочисленным и определенным при помощи библиотеки numpy).

import numpy as np
a = np.zeros(5)
def umnojenie(a):
    v = 1
    for i in range(len(a)):
        a[i] = int(input())
        v *= a[i]
    return v
print(umnojenie(a))