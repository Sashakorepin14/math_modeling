import time

a = 5
b = 4
c = 7
d = 3
e = 2

def hz(x):
    return a * x**4 + b * x**3 + c * x**2 + d * x + e

n = 10**5

st_time = time.time()
map = list(map(hz, range(n)))
maptime = time.time() - st_time

st_time = time.time()
listcomp = [hz(x) for x in range(n)]
listcomptime = time.time() - st_time

st_time = time.time()
a = []
for x in range(n):
    a.append(hz(x))
cycletime = time.time() - st_time

print(maptime)
print(listcomptime)
print(cycletime)