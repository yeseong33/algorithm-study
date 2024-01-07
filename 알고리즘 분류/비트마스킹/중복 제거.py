import sys
nums = map(int, sys.stdin.readline().split())
k = 0
for i in nums:
    if k & (1<<i) == 0:
        print(i, end=' ')
        k = k | (1<<i)

