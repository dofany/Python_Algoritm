from math import sqrt

m,n = map(int,input().split())

result = []
for i in range(m,n+1):
    count = 0
    if i == 1:
        count = 1
    n2 = int(sqrt(i)) + 1
    for j in range(2,n2):
        if i%j == 0:
            count = 1
            break
    if count == 0:
        result.append(i)
        print(i)