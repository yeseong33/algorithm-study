import sys

n = int(input())

nums = [0, 1, 2] + [0] * 998

def dp(n):
    if n == 1:
        return nums[1]
    if n == 2: 
        return nums[2]
    
    for i in range(3, n+1):
        nums[i] = nums[i-1] + nums[i-2]%10007
    
    return nums[n]

print(dp(n))
