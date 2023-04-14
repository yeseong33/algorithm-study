import sys

n = int(input())
m = int(input())
nums = list(map(int, sys.stdin.readline().split()))
nums.sort()


def point(left, right, x):
    count = 0
    
    while left != right:
        
        sum = nums[left] + nums[right]

        if sum == x:
            count += 1
            left += 1
        elif sum > x:
            right -= 1
        elif sum < x:
            left += 1
    return count 

c = point(0, n-1, m)

print(c)
