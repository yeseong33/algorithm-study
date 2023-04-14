import sys

n = int(input())

nums = list(map(int, sys.stdin.readline().split()))
nums.sort()


x = int(input())


def point(left, right, x):
    
    count = 0 
    
    while right != left:
        sum = nums[left] + nums[right]
        
        if sum == x:
            count += 1
            left += 1
        elif sum > x:
            right -= 1
        elif sum < x:
            left += 1           
            
    return count

c = point(0, n-1, x)
print(c)