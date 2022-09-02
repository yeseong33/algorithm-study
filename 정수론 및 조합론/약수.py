import sys 


# 1 3 9 27 81


n = int(sys.stdin.readline())

nums = list(map(int, sys.stdin.readline().split()))


N = max(nums) * min(nums)
    
print(N)