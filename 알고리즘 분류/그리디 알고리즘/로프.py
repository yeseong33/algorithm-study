import sys

n = int(input())

min = 10001
nums = []
for i in range(n):
    k = int(sys.stdin.readline().strip())
    nums.append(k)
nums.sort()


ans = []
for i in range(n):
    k = nums[i] * (n-i)
    ans.append(k)
print(max(ans))
    
    


