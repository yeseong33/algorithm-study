n = int(input())

nums = [0, 0, 3, 0, 11] + [0] * 28

def dp(n):
    
    for i in range(6, n+1, 2):
        total = 2
        for j in range(2, i-3, 2):
            total += nums[j] * 2
        nums[i] = 3*nums[i-2] + total
        
dp(n)
print(nums[n])        

     
    
    