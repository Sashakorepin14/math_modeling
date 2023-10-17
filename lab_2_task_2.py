b1 = int(input('Введите первй член '))
q = int(input('Введите знаменатель '))
n = int(input('Введите количество членов '))
v = 1
b = b1*(q**(v-1))
for n in range(0, n, 1):
    print('b = ', b1*(q**(v-1)))
    v = v + 1