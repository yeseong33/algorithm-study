import sys

n, k = map(int, sys.stdin.readline().split())

nums = [[1] * n]
for i in range(k-1):
    nums.append([0] * n )



for i in range(1, k):
    for j in range(n):
        if j == 0:
            
            nums[i][j] = i+1
        else:
            nums[i][j] = nums[i-1][j] + nums[i][j-1]
print(nums[k-1][n-1]%1000000000)