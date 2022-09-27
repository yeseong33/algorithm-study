import sys

# n = int(input())
list_1 = list(map(int,sys.stdin.readline().split()))
grape = list_1[1:]
n = list_1[0]

# grape = [int(sys.stdin.readline().strip()) for i in range(n)] + [0] * 2
nums = [0] * (n+2)
nums[0] = grape[0]
nums[1] = nums[0] + grape[1]
nums[2] = max(grape[2] + grape[0], grape[2] + grape[1], nums[1])

for i in range(3, n):
    if grape[i-1] == 0:
        nums[i] = nums[i-1] + grape[i]
    else:
        nums[i] = max(grape[i]+grape[i-1]+nums[i-3], nums[i-2] + grape[i], nums[i-1])

print(max(nums))



