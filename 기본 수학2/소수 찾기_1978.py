n = int(input())
m = list(map(int,input().split()))
result = 0

for i in m:
    f = True
    if i <= 1:
        continue
    for j in range(2,i):
        if i%j == 0:
            f = False
            break
    if f:
        result += 1
print(result)