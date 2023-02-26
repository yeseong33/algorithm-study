import sys

n = int(input())

# point의 공간이 두개 더 필요한 이유
# 밑에서 미리 저장해 주기 위한 point[2] 을 만족하기 위해서 
point = [0] * (n+2)
nums = []
for i in range(n):
    nums.append(int(input()))
# nums 공간이 두개 더 필요한 이유
# n = 1 일 때 nums[2],을 지원하지 못함
nums = nums + [0] * 2
    
point[0] = nums[0]
point[1] = nums[1] + nums[0]
point[2] = max(nums[0]+nums[2], nums[1] + nums[2])


for i in range(3, n):
    point[i] = max(nums[i] +nums[i-1] +point[i-3], nums[i] + point[i-2])
        

print(point[n-1])
    
    