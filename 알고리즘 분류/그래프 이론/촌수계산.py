import sys
from collections import deque

n = int(input())

x, y = map(int, sys.stdin.readline().split())


m = int(input())

graph = [[] for i in range(n+1)]

for i in range(m):
    a, b =  map(int, sys.stdin.readline().split())
    graph[a].append(b)
    graph[b].append(a)


def solution(G, x, y):
    
    q = deque()
    q.append([x,0])
    visited = [0] * (n+1)
    
    while q:
        now, lev = q.popleft()
        
        if now == y:
            return lev
        
        for i in graph[now]:
            if not visited[i]:
                visited[i] = 1
                q.append([i, lev+1])
                
    return -1

k = solution(graph, x, y)
print(k)
