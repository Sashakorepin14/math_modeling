def func():
    print('1. рассеивающая')
    print('2. собирающая')
    a = int(input())
    print('растояние от предмета')
    b = float(input())
    print('фокусное расстояние')
    c = float(input())

    if a == 1:
        if b < c:
            return "Уменьшенное, действительное, прямое"
        elif b == c:
            return "Нет изображения"
        else:
            return "Увеличенное, действительное, обратное"
    elif b == 2:
        if b < c:
            return "Увеличенное, мнимое, прямое"
        elif b == c:
            return "Нет изображения"
        else:
            return "Уменьшенное, мнимое, обратное"
    else:
        print('Ошибка')
print(func())