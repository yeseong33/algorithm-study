import sys
from collections import deque


n, k = map(int, sys.stdin.readline().split())



def bfs(n):
    q = deque()
    q.append((n, 0))
    
    find = 100001
    count = 0
    nums = [0] * 100001
    while q:
        now, sec = q.popleft()
        
        if sec > find: 
            continue
        
        if now == k:
            if find == 100001:
                find = sec
            if sec == find:
                count += 1
        
        d  = [now +1, now-1, now*2]
        
        for i in d:
            if 0 <= i <= 100000  and (nums[i] == 0 or nums[i] == sec+1):
                nums[i] = sec+1
                q.append((i, sec+1))
                
    return count, find

c, f = bfs(n)



print(f)
print(c)
        