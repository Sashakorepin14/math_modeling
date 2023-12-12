import time

def cycle(M, N):
    timer = time.time()
    b = 0
    for i in range(M):
        for j in range(N):
            b += 1
            print(b)
            time.sleep(1)
    a = (f'{time.time() - timer}, seconds')
    return a
print(cycle(3, 2))