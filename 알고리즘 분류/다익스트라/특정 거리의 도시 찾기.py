# import sys
# from collections import deque

# # BFS
# n, m, k, x = map(int, sys.stdin.readline().split())

# graph = [[] for i in range(n+1)]

# for i in range(m):
#     a, b = map(int, sys.stdin.readline().split())
#     graph[a].append(b)
    
    
# def solution(x, k):
#     q = deque()
#     q.append((x, 0))
#     visited = [0] * (n+1)
#     visited[x] = 1
#     ans = []
#     lev = 0
#     while q and lev < k+1:
#         now, lev = q.popleft()
        
#         if lev == k:
#             ans.append(now)
            
#         for i in graph[now]:
#             if not visited[i]:
#                 visited[i] = 1
#                 q.append((i, lev+1))
#     return ans                
# ans = solution(x, k)

# if ans == []:
#     print(-1)
# else:
#     ans.sort()
#     for i in ans:
#         print(i)

# 다익스트라
import sys, heapq
INF = int(1e10)
n, m, k, x = map(int, sys.stdin.readline().split())

graph = [[] for i in range(n+1)]

for i in range(m):
    a, b = map(int, sys.stdin.readline().split())
    graph[a].append(b)


def solution(start):
    distance = [INF] * (n+1)
    q = []
    heapq.heappush(q,(0, start))
    distance[start] = 0
    while q:
        dis, now = heapq.heappop(q)
        
        if distance[now] < dis:
            continue
        
        for i in graph[now]:
            cost = dis + 1
            if cost < distance[i]:
                distance[i] = cost
                heapq.heappush(q, (cost, i))
    return distance

a = solution(x)
ans = []            
for i in range(1, n+1):
    if a[i] == k:
        ans.append(i)

if ans == []:
    print(-1)
else: 
    ans.sort()
    for i in ans:
        print(i)