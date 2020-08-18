h,m = map(int,input().split())

m = m-45

if m < 0 :
  h = h-1
print(h%24,m%60)
