a = int(input('Введите год '))
b = a % 4
c = a % 100
d = a % 400
if b == 0 and d == 0 or c != 0:
    print('Високосный')
else:
    print('Невисокосный')