import sys

n = int(input())

m = int(input())

if m != 0:
    broken = list(map(int, sys.stdin.readline().split()))
else:
    broken = []

min_count = abs(100-n)

for nums in range(1000001):
    nums = str(nums)
    
    for j in range(len(nums)):
        if int(nums[j]) in broken:
            break
        
        if j == len(nums)-1:
            min_count = min(min_count, abs(int(nums) - n) + len(nums))
            
print(min_count)
        