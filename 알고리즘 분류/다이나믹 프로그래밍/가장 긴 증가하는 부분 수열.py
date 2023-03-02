import sys
# sys.setrecursionlimit(10 ** 5)
# from collections import deque

n = int(input())

nums = list(map(int, sys.stdin.readline().split()))

count = [1] * n

for i in range(n):
    for j in range(i):
        if nums[i] > nums[j]:
            
            if count[j] + 1 > count[i]:
                count[i] = count[j] + 1
                
mc = max(count)
p2 = []
c = mc
for i in range(n-1, -1, -1):
    if count[i] == c:
        p2.append(nums[i])
        c -= 1
        
p2.reverse()
print(mc)
print(*p2)

# 3
# 3 1 2
# 5
# 1 4 2 3 5
