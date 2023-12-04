import sys, math

n = int(input())
nums = list(map(int, sys.stdin.readline().split()))
a, b = map(int, sys.stdin.readline().split())

count = 0
for i in nums:
    if i-a <= 0: 
        count += 1
    else: 
        tmp = math.ceil((i-a)/b)
        count += 1 + tmp
print(count)