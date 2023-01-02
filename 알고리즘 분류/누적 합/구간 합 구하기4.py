import sys

n, m = map(int, sys.stdin.readline().split())

arr = list(map(int, sys.stdin.readline().split()))
nums = [0]
k = 0 

for i in arr:
    k += i
    nums.append(k)

for _ in range(m):
     i, j = map(int, sys.stdin.readline().split())
     k = nums[j] - nums[i-1]
     print(k)
     
        
