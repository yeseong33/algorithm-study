# 1) 
import sys

n = int(sys.stdin.readline())

ans = [0] * n

x = list(map(int, sys.stdin.readline().split()))
x_remove = x.copy()


for _ in range(n):
    m = min(x_remove) 
    for i in range(n):
        if x[i] > m and x.count(m) == 1:
            ans[i] += 1 
        elif x[i] > m and x.count(m) != 1:
            nums = x.count(m)
            ans[i] += 1/nums
    x_remove.remove(m)        

for i in range(n):
    print(int(ans[i]), end=' ')




# 2) 
import sys

n = int(sys.stdin.readline())

ans = [0] * n


x = list(map(int, sys.stdin.readline().split()))
x_c = x.copy()
x_d = {}
for i in x:
    x_c[i] = 0


x = list(set(x))
x.sort()


for i in range(len(x)):
    x_d[x[i]] = i
    
    
for i in range(n):
    print(x_d[x_c[i]], end = ' ')



