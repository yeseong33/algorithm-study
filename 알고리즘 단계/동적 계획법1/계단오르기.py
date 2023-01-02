import sys

n = int(input())

nums = [int(sys.stdin.readline()) for _ in range(n)]+ [0] * 3
memo = [0] * (n+2)

# [10, 30, 35, ]

memo[0] = nums[0]
memo[1] = nums[0] +nums[1]
memo[2] = max(nums[0]+ nums[2], nums[1]+nums[2])

for i in range(3, n):
    memo[i] = max(memo[i-3]+nums[i]+nums[i-1], memo[i-2]+nums[i])

print(memo[n-1])

## 공유기설치