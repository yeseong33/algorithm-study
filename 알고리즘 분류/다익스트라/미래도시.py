# 1 -> k -> x 2번 실행
import sys, heapq
INF = int(1e9)
n, m = map(int, sys.stdin.readline().split())

graph = [[] for _ in range(n+1)]

for i in range(m):
    a, b = map(int, sys.stdin.readline().split())
    graph[a].append(b)
    graph[b].append(a)
    
x, k = map(int, sys.stdin.readline().split())
    

def dix(start):
    q = []
    heapq.heappush(q, start)
    
    visited = [False] * 101
    com = [INF] * 101
    
    com[start] = 0
    
    while q:
        now = heapq.heappop(q)
        
        if visited[now]:
            continue
        visited[now] = True
        
        for i in graph[now]:
            cost = com[now] + 1
            if cost < com[i]:
                com[i] = cost
                heapq.heappush(q, i)
    return com

total = 0
com = dix(1)
total += com[k]

com = dix(k)
total += com[x]

print( total)
# 
# 5 7 
# 1 2 
# 1 3 
# 1 4
# 2 4
# 3 4 
# 3 5 
# 4 5
# 4 5