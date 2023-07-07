import sys
import heapq
from collections import deque
INF = int(1e10)

n, m = map(int, sys.stdin.readline().split())

graph = [[] for i in range(n+1)]
for i in range(m):
    a, b, c = map(int, sys.stdin.readline().split())
    graph[a].append([c, b])
    graph[b].append([c, a])

for i in range(1, n+1):
    graph[i].sort(reverse=True)

x, y = map(int, sys.stdin.readline().split())


def solution(x, y):
    q = []
    heapq.heappush(q, (0, x))
    costs = [0] * (n+1)

    while q:
        cost, now = heapq.heappop(q)
        cost = -cost
        
        if now == y:
            print(cost)
            return
        
        if costs[now] > cost:
            continue
        
        
        for i in graph[now]:
            c, next = i[0], i[1]
            if cost == 0:
                costs[next] = c
                heapq.heappush(q, (-c, next))
                
            elif costs[next] < c and costs[next] < cost:
                costs[next] = min(cost, c)
                heapq.heappush(q, (-costs[next], c))


solution(x, y)


                    
        