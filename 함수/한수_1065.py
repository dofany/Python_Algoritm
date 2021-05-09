n = int(input())
sum = 0
for i in range(1,n+1):
    if i <= 99:
        sum += 1
    else:
        nums = list(map(int, str(i)))
        if nums[0]-nums[1] == nums[1]-nums[2]:
            sum +=1
print(sum)