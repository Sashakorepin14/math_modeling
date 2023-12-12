import time
import random

def cycle():
    N = random.randint(1, 10)
    M = random.randint(1, 10)
    print(N)
    print(M)
    timer = time.time()
    b = 0
    for i in range(M):
        for j in range(N):
            b += 1
            print(b)
            time.sleep(1)
    a = (f'{time.time() - timer}, seconds')
    return a
print(cycle())