# x 2 + y 2 =< r 2
import sys





n = int(sys.stdin.readline())


for _ in range(n):
    nums = list(map(int, sys.stdin.readline().split()))
    s = []
    e = []
    
    for i in range(4):
        if i < 2:
            s.append(nums[i])
        else:
            e.append(nums[i])
        
    h = int(input())
    s_ans = [0] * h
    e_ans = [0] * h
    c = 0
    for j in range(h):
        x, y, r = map(int, sys.stdin.readline().split())
        if (s[0]-x)**2 + (s[1]-y) ** 2 <= r**2:
            s_ans[j] += 1
        if (e[0]-x)**2 + (e[1]-y) ** 2 <= r**2:
            e_ans[j] += 1
    
    for k in range(h):
        if s_ans[k] != e_ans[k]:
            c += 1
    print(c)
            
        
        