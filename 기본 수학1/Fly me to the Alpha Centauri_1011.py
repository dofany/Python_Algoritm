import math

t = int(input())

for i in range(t):
    a,b = map(int,input().split())
    c = b-a
    d = math.sqrt(c)
    e = math.floor(d)
    f = e**2+e

    if e**2 < c <= f:
        print(e*2)
    elif e**2 <= c <= f:
        print(2*e-1)
    elif f < c <=(e+1) **2:
        print(2*e+1)
