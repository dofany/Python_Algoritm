n = int(input())

for i in range(n//3+1):
    if n % 5 == 0:
        print(i+n//5)
        break
    n = n-3
    if n < 0:
        print(-1)