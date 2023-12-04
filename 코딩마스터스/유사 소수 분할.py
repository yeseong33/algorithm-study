# -*- coding: utf-8 -*-
import sys, math

n = int(sys.stdin.readline())
so = []
# 소수 판별
def is_prime(x):
    for i in range(2, int(math.sqrt(x) + 1)):
        if x % i == 0:		
            return False
    so.append(x)
    return True
for i in range(1, n):
    is_prime(i)
most_so = []
for i in range(1, n):
    nums = []
    for j in range(1, i+1):
        if i%j == 0:
            nums.append(j)
    nums.sort()
    if len(nums) == 4 and nums[1] in so and nums[2] in so:
        most_so.append(i)
visited = []
t = []
def dfs():
    
    if len(visited) == 3:
        k = sum(visited)
        if k < n:
            return True
        return False
    
    for i in range(len(most_so)):
        if most_so[i] not in visited:
            visited.append(most_so[i])
            if dfs():
                return True 
            visited.pop()
    return False

if dfs():
    print('possible')
else:
    print('impossible')