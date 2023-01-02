import sys

n = int(sys.stdin.readline())

nums = [0] * 10001

for i in range(n):
    nums[int(sys.stdin.readline())] += 1
    
for i in range(10001):
    for n in range(nums[i]):
        print(i)
        