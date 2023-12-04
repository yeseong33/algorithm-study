import sys, math

input = sys.stdin.readline

n = int(input())
if n%3==0:
    nh = n//3+1
else:
    nh = n//3 + n%3
nums = [0] * (n+1)

for a in range(1, n):
    for b in range(a, n):
        c = math.sqrt(a**2 + b**2)
        if c.is_integer() and a+b+c <= n:
            if a+b > c and c > a and c > b:
                nums[int(a+b+c)] += 1 
k = max(nums)          
print(nums.index(k), k)