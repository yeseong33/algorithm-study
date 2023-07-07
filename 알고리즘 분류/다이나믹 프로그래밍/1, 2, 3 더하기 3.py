import sys

n = int(input())

id = []

for i in range(n):
    k = int(sys.stdin.readline().strip())
    id.append(k)

m = max(id)

nums = [0] * (m +1)
nums[1] = 1
nums[2] = 2
nums[3] = 4

for i in range(4, m+1):
    nums[i] = nums[i-1] % 1000000009 + nums[i-2] % 1000000009 + nums[i-3] % 1000000009

for i in id:
    print(nums[i]% 1000000009)