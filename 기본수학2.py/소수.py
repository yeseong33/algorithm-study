import sys

m = int(sys.stdin.readline())
n = int(sys.stdin.readline())
nums =[] 

for i in range(m, n+1):
    c = 0
    for j in range(2, i):
        if i % j == 0:
            c += 1
            break
    if c == 0 and i != 1:
        nums.append(i)
        
if len(nums) > 0:
    print(sum(nums))
    print(nums[0])
else:
    print(-1)
  
  
        
##
a = [False, False] + [True] * 9999
n = int(input())

for i in range(2, n):
    if a[i]:
        for j in range(i*2, 10001, i):
            a[j] = False
so = [i for i in range(len(a)) if a[i]]
print
