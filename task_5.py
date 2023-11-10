import task_4 as t4
c1 = int(input("Один столбец: "))
c2 = int(input("Другой столбец: "))
for i in range(t4.N):
    t4.NxM[i, c1], t4.NxM[i, c2] = t4.NxM[i, c2], t4.NxM[i, c1]
    print(t4.NxM[i])