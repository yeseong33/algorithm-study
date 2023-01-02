import sys

cam = int(sys.stdin.readline().strip())

max_1 = 0
max_2 = 0
max_idx_1 = 0
max_idx_2 = 0

nums = []

for i in range(6):
    a, b= map(int, sys.stdin.readline().split())
    nums.append(b)


max_1 = max(nums)
max_idx_1 = nums.index(max_1)


# [10, 10, 20 , 20 , 30, 30]
if nums[max_idx_1-1] > nums[max_idx_1-5]:
    max_2 = nums[max_idx_1-1]
    max_idx_2 = max_idx_1-1
    x = nums[max_idx_2 -2] * nums[max_idx_2 -3]
        
elif nums[max_idx_1-1] < nums[max_idx_1-5]:
    max_2 = nums[max_idx_1-5]
    max_idx_2 = max_idx_1-5
    x = nums[max_idx_1 -2] * nums[max_idx_1 -3]
        

    
area = max_1 * max_2 - x

print(area * cam)


##
# 1
# 4 10
# 2 10
# 4 20
# 2 20
# 3 30
# 1 30
# 700
