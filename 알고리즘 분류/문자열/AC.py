import sys
from collections import deque

t = int(input())

def AC(nums, f):
    count = 0
    for i in f:
        if count%2 == 0 and i == 'D':
            if not len(nums):
                return ''
            nums.popleft()
        elif count%2 == 1 and i == 'D':
            if not len(nums):
                return ''
            nums.pop()
        elif i == 'R':
            count += 1
    if count%2 == 1:
        nums = list(nums)
        nums = nums[-1::-1]
    return nums

delete = set({'[', ']', ','})
tt = False
for i in range(t):
    f = sys.stdin.readline().strip()
    n = sys.stdin.readline().strip()
    s = sys.stdin.readline().strip()
    nums = deque()
    p = ''
    for i in s:
        if i == ',' or i == ']':
            tt = True
        if i not in delete and not tt:
            p += i
        elif tt:
            if p != '':
                nums.append(p)
            p = ''
            tt = False
    k = AC(nums, f)
    if k == '':
        print('error')
    else:
        print('[' + ','.join(k) + ']')
    
# from collections import deque

# a = deque()
# k1 = a.popleft()
# k2 = a.pop()
# print(k1, k2)
