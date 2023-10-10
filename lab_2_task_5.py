a = int(input('Введите первое число '))
b = int(input('Введите второе число '))
c = a % b
d = a // b
if c == 0 and b != 0:
    print(d)
elif c != 0 and b != 0:
    print(d, ';', c)
elif b == 0:
    print('На ноль делить нельзя')