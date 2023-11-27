import numpy as np
g = 9.8

def meh_en():
    m = float(input('масса '))
    h = float(input('высота полета '))
    v = float(input('скорость тела '))
    k = m * g * h
    p = (m * (v**2)) / 2
    meh = k + p
    return meh
print(meh_en())