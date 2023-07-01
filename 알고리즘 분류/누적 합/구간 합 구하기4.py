import sys

n, m = map(int, sys.stdin.readline().split())

nums = list(map(int, sys.stdin.readline().split()))

# 구간합 구해놓기
nums_hap = [0] * (n + 1)
total = 0

for i in range(1, n+1):
    total += nums[i-1]
    nums_hap[i] = total


for _ in range(m):
    i, j = map(int, sys.stdin.readline().split())
    print(nums_hap[j] - nums_hap[i-1])