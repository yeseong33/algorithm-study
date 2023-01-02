import sys

n, m = map(int,sys.stdin.readline().split())

nums = {}
name = {}

for i in range(1, n+1):
    k = sys.stdin.readline().strip()
    nums[i] = k
    name[k] = i

ans = []
for i in range(m):
    k = sys.stdin.readline().strip()    
    if k.isdigit():
        k = int(k)
        ans.append(nums[k])
    else:
        ans.append(name[k])

for i in ans:
    print(i) 