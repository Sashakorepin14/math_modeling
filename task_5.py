import numpy as np
p = 3.14

def plohad():
    print('1. Круг')
    print('2. Треугольник')
    print('3. Прямоугольник')
    t = int(input())
    if t == 1:
        R = float(input())
        P = p * (R**2)
    elif t == 2:
        a = float(input())
        ha = float(input())
        P = (a * ha)/2
    elif t == 3:
        a = float(input())
        b = float(input())
        P = a * b
    return P
print(plohad())