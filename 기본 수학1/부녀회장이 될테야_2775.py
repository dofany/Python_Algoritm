t = int(input())
for i in range(t):
    k = int(input())
    n = int(input())

    a = [j for j in range(1,n+1)]

    for l in range(k):
        for m in range(1,n):
            a[m] += a[m-1]
    print(a[n-1])
