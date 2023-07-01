import sys

n = int(input())

nums = list(map(int, sys.stdin.readline().split()))
dp = [1] *n
visited = [0] * 1001
for i in range(n):
    for j in range(i, n):
        if nums[i] < nums[j]:
            dp[j] = max(dp[i] + 1, dp[j])
            
print(max(dp))