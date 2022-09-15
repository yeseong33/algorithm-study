import sys 

n = int(input())

nums = list(map(int, sys.stdin.readline().split()))
k = 0
total = 0
maxi = -1001 * 100000

# 10
# a = [10, -4, 3, 1, 5, 6, -35, 12, 21, -1]
#           6  9  10 15 21 -14  
#                               12  33  32 

# a = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, -100, 20]


while k != len(nums):
    
    total += nums[k]
    
    if total > maxi:
        maxi = total
    if total < 0:
        total = 0
    k += 1


print(maxi)
        
        
        