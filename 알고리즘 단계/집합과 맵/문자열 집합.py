import sys

n, m = map(int, sys.stdin.readline().split())

ns = set()

ns = { sys.stdin.readline().strip() for _ in range(n) }

ms_l = [sys.stdin.readline().strip() for _ in range(m)]

ms = set(ms_l)

a = ns & ms

c = 0

for i in range(m):
    if ms_l[i] in a:
        c += 1
    
print(c)