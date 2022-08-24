import sys

n = int(sys.stdin.readline().strip())

nums_l = list(map(str, sys.stdin.readline().split()))
nums_s = set(nums_l)
nums_d = {}


for i in nums_s:
    nums_d[i] = 0

for i in nums_l:
    nums_d[i] += 1
    
m = int(sys.stdin.readline().strip())

nums_l_2 = list(map(str, sys.stdin.readline().split()))
nums_s_2  = set(nums_l_2)

a = nums_s & nums_s_2

for i in nums_l_2:
    if i in a: 
        print(nums_d[i], end = ' ')
    else:
        print(0, end = ' ')