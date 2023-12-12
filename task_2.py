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

    b_str1 = '_'.join(a)
    bhz2 = b_str1.lower()
    h2 = []
    name2 = name.lower()
    for i in name2:
        h2.append(ord(i))\
        
    l1 = (f'{max(h)}, максимальное значение первого списка')
    l2 = (f'{max(h2)}, максимальное значение второго списка')



    return a, b_str, bhz1, h, bhz2, h2, l1, l2

print(hz('Aleksandr Korepin'))