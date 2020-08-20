a = int(input())

for i in range(a):
  i = i+1
  b,c = map(int,input().split())
  print("Case #%d: %d + %d = %d" %(i,int(b),int(c),int(b)+int(c)))