import sys

n = int(input())

nums = []

for i in range(n):
    k = int(sys.stdin.readline().strip())
    nums.append(k)

dp = [1] * n


for i in range(n):
    for j in range(i, n):
        if nums[i] < nums[j]:
            dp[j] = max(dp[j], dp[i] + 1)
            
print(n-max(dp))