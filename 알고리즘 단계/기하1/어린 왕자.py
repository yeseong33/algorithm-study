import sys

n = int(sys.stdin.readline())


for _ in range(n):
    s1, s2, e1, e2 = list(map(int, sys.stdin.readline().split()))
        
    h = int(input())
    s_ans = [0] * h # [1, 1, 0, 1, 0, 0, 0]
    e_ans = [0] * h # [0, 1, 1, 0, 0, 0, 0]
    c = 0
    
    for j in range(h):
        x, y, r = map(int, sys.stdin.readline().split())
        if (s1-x)**2 + (s2-y) ** 2 <= r**2:
            s_ans[j] += 1
        if (e1-x)**2 + (e2-y) ** 2 <= r**2:
            e_ans[j] += 1
    
    for k in range(h):
        if s_ans[k] != e_ans[k]:
            c += 1
            
    print(c)