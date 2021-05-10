a = input().split()
result = a[0]
result1 = a[1]
if int(result[::-1]) > int(result1[::-1]):
    print(result[::-1])
else:
    print(result1[::-1])