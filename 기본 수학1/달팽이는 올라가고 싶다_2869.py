A,B,V = map(int,input().split())
result = 0

V -= A
A -= B
if V%A == 0:
    print((V//A)+1)
else:
    print((V//A)+2)

