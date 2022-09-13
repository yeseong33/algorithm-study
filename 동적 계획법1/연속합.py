import sys 

n = int(input())

nums = list(map(int, sys.stdin.readline().split()))
k = 0
total = 0
maxi = -1001 * 100000


while k != len(nums):
    
    total += nums[k]
    
    if total > maxi:
        maxi = total
    if total < 0:
        total = 0
    k += 1


print(maxi)
        
        
        