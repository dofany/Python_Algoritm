# 1 = " "
# 2 = a,b,c
# 3 = d,e,f
# 4 = g,h,i
# 5 = j,k,l
# 6 = m,n,o
# 7 = p,q,r,s
# 8 = t,u,v
# 9 = w,x,y,z
# 0 = operator

lst = ['ABC','DEF','GHI','JKL','MNO','PQRS','TUV','WXYZ']
n = input()
delay = 0

for i in lst:
    for j in i:
        for k in n:
            if j == k :
                delay += lst.index(i) +3  # time = time + index +3
print(delay)

