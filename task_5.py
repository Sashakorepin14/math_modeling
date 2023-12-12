def fio(fio):
    a = [ord(char) for char in fio.upper()]
    b = [ord(char) for char in fio.lower()]
    sum1 = sum(a)
    sum2 = sum(b)
    return sum1, sum2
print(fio('Корепин Александр Сергеевич'))