import sys

n, s = map(int, sys.stdin.readline().split())
arr = list(map(int, sys.stdin.readline().split()))
nums = [0]
k = 0
lenth = len(arr)+1
start = 0
end = 0

# 5 1 3 5 10 7  4  9  2  8
# 0 5 6 9 14 24 31 35 44 46 54

for i in arr:
    k += i
    nums.append(k)


while True:
    gap = nums[end] - nums[start]
    if gap >= s:
        if lenth > end - start:
            lenth = end - start
        start += 1
    elif end == len(nums)-1:
        start += 1
    elif gap < s:
        end += 1
        
    if start == len(nums)-1:
        break
    
if lenth == len(arr)+1:
    print(0)
else:
    print(lenth)