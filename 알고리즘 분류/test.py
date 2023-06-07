import sys
from collections import deque

t = int(input())


def wi(id, mt, g):
    q = deque()
    takeTime = [0] * (n+1)
    visited = [0] * (n+1)

    for i in range(1, n+1):
        if not id[i]:
            q.append(i)
            visited[i] = 1
            takeTime[i] += mt[i]
            
    while q:
        now = q.popleft()
        
        for i in g[now]:
            id[i] -= 1
            if takeTime[i] < takeTime[now]:
                takeTime[i] = takeTime[now] 
        
        for i in range(1, n+1):
            if not id[i] and not visited[i]:
                q.append(i)
                visited[i] = 1
                takeTime[i] += mt[i]
                
    return takeTime


for _ in range(t):
    n, k = map(int, sys.stdin.readline().split())
    makeTime = [0] + list(map(int, sys.stdin.readline().split()))
    
    graph = [[] for i in range(n+1)]
    indegree = [0] * (n+1)
    
    for i in range(k):
        a, b = map(int, sys.stdin.readline().split())
        graph[a].append(b)
        indegree[b] += 1
    
    w = int(input())
    takeTime = wi(indegree, makeTime, graph)
    print(takeTime[w])
    