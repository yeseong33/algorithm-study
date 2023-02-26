n = int(input())

nums = [0, 1, 3] + [0] * 999

def dp(n):
    
    for i in range(3, n+1):
        nums[i] = nums[i-1]+ 2 * nums[i-2]
    
    return nums[n]

print(dp(n)%10007)