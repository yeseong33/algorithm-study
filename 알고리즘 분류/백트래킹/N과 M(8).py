import sys

n, m = map(int, sys.stdin.readline().split())

nums = list(map(int, sys.stdin.readline().split()))

nums.sort()

tmp = [0]

def BT():
    
    if len(tmp) == m+1:
        print(*tmp[1:])
        return
    
    for i in range(n):
        if tmp[-1] <= nums[i]:
            tmp.append(nums[i])
            BT()
            tmp.pop()

BT()