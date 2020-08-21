n,x = map(int,input().split())
a = input().split()
ret = ""
for i in range(n):
  if int(a[i]) < x:
    ret += a[i] + " "
print(ret)