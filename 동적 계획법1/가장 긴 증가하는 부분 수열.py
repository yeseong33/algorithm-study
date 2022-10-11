import sys

n = int(input())

nums = list(map(int, sys.stdin.readline().split()))
count = [1] * n
print(nums)
# answer
# 18 23 53 60 77 83 85
# 1  1  1  1  1  1  1  
# 10 20 10 30 20 50
# 1  2  1  3  2   4 

for i in range(n):
    for j in range(i):
        if nums[i] > nums[j]:
            if count[i] < count[j] + 1:
                 count[i] = count[j] + 1

print(count)       
print(max(count))       
            
