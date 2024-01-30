N = int(input())
if N < 1 or N > 31:
    print('Неверное кол-во дней')
else:
    list = []
    a = 0
    for i in range(N):
        list.append(int(input()))
        if list[i] >= 0:
            a += 1
    if a > 4:
        print('Yes')
    else:
        print('No')