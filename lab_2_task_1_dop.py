import math

a = int(input('Введите первый коэффициент:'))
b = int(input('Введите второй коэффициент:'))
c = int(input('Введите свободный член:'))
d = b**2 + -4*a*c
if d > 0:
    print('x = ',-1*b + math.sqrt(d),'/',2*a)
    print('x = ',-1*b - math.sqrt(d),'/',2*a)
elif d == 0:
    print('x = '-1*b,'/',2*a)
elif d < 0:
    print('НЕТ РЕШЕНИЙ!')