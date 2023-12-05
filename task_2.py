import numpy as np

def hz(name):
    a = ''
    for i in name:
        a += str(i)
    b_str = '_'.join(a)
    bhz1 = b_str.upper()
    for i in name:
        h = []
        h += int(ord(i))



    return a, b_str, bhz1, h

print(hz('Aleksandr Korepin'))