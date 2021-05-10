n = int(input())
count = 0

for i in range(n):
    t = input()
    for j in range(len(t)):
        if j != len(t)-1:
            if t[j] == t[j+1]:
                continue
            elif t[j] in t[j+1:]:
                break
        else:
            count += 1
print(count)