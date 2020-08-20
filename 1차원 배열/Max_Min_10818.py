import sys
n = int(input())
num = sys.stdin.readline()
nums = list(map(int,num.split(" ")))

print("{} {}".format(min(nums),max(nums)))