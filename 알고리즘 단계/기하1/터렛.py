import sys, math

n = int(input())
for i in range(n):
    nums = list(map(int, sys.stdin.readline().split()))
    r1 =nums[2]
    r2 =nums[5]
    
    R = abs(nums[0] - nums[3])**2 + abs(nums[1] - nums[4])**2
    if R == 0 and r1 == r2:
        print(-1)
    elif R > (r1 + r2)  ** 2 or R < abs(r1 - r2) ** 2:
        print(0)
    elif R == (r1 + r2) ** 2 or R == abs(r1-r2) ** 2:
        print(1)
    else:
        print(2)
  