import numpy as np

def hz(name):
    a = ''
    for i in name:
        a += str(i)
    b_str = '_'.join(a)
    bhz1 = b_str.upper()
    h = []
    name1 = name.upper()
    for i in name1:
        h.append(ord(i))

    
    a1 = ''
    for i in name:
        a1 += str(i)
    b_str1 = '_'.join(a)
    bhz2 = b_str1.lower()
    h2 = []
    name2 = name.lower()
    for i in name2:
        h2.append(ord(i))



    return a, b_str, bhz1, h, a1, bhz2, h2

print(hz('Aleksandr Korepin'))