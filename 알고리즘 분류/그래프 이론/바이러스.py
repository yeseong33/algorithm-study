import sys
from collections import deque
n = int(input())

m = int(input())

graph = [[] for _ in range(n+1)]

for i in range(m):
    a, b = map(int, sys.stdin.readline().split())
    graph[a].append(b)
    graph[b].append(a)



def BFS():
    q = deque()
    q.append(1)
    visited = [0] * (n+1)
    
    while q:
        node = q.popleft()
        for i in graph[node]:
            if visited[i] == 0:
                visited[i] = 1
                q.append(i)
            
    return visited

v = BFS()
count = 0
for i in v[2:]:
    if i == 1:
        count += 1
print(count)
