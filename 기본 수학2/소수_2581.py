m = int(input())
n = int(input())

result = []
for i in range(m,n+1):
    count = 0
    if i > 1:
        for j in range(2,i):
            if i%j == 0:
                count = 1
                break
        if count == 0:
            result.append(i)

if len(result) != 0:
    print(sum(result))
    print(min(result))
else:
    print(-1)