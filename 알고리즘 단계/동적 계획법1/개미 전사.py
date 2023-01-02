n = int(input())

nums = list(map(int, input().split()))

d = [0] * 100

d[0] = nums[0]
d[1] = max(nums[0], nums[1])

for i in range(2, n):
    d[i] = max(d[i-1],d[i-2] + nums[i])

print(d[n-1])