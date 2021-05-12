n = int(input())
start = 1
end = 6
result = 1

while(True):
    if(n<=start):
        break
    start += end
    end += 6
    result += 1

print(result)