import sys
n = int(input())
for i in range(n):
  num = sys.stdin.readline()
  nums = list(map(int,num.split(" ")))
print(nums)

