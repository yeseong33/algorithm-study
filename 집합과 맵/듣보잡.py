import sys

n, m = map(int, sys.stdin.readline().split())

h = set()
s = set()
ans = []
for i in range(n):
    k = sys.stdin.readline().strip()
    h.add(k)

for i in range(m):
    k = sys.stdin.readline().strip()
    s.add(k)

for i in h:
    if i in s:
        ans.append(i)

ans.sort()

print(len(ans))
for i in range(len(ans)):
    print(ans[i])
    
 