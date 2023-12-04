# import sys
# import heapq

# find = []

# def solution(n, paths, gates, summits):
#     global find
#     INF = int(1e9)
#     graph = [[] for i in range(n+1)]

#     for a, b, c in paths:
#         graph[a].append((b, c))
#         graph[b].append((a, c))
        
#     gates = set(gates)
#     summits = set(summits)
#     def dix(start):
#         global find
        
#         q = []
#         heapq.heappush(q, (0, start))
#         visited = [0] * (n+1)
#         visited[start] = 1 
#         while q:
#             intensity, now = heapq.heappop(q)
#             if now != start and now in gates: continue
#             if now != start and visited[now]: continue
#             if find != [] and find[1] < intensity: continue
#             if now in summits: 
#                 if find == []:
#                     find = [now, intensity]
#                 else:
#                     if find[1] > intensity:
#                         find = [now, intensity]
#                 continue
                    
#             visited[now] = 1

#             for next, cost in graph[now]:
#                 if not visited[next]:
#                     next_cost = max(cost, intensity)
#                     heapq.heappush(q, (next_cost, next))
#     for i in gates:
#         dix(i)
#         print(i)
#         print(find)
#     answer = []
#     return answer
# solution(6, [[1, 2, 3], [2, 3, 5], [2, 4, 2], [2, 5, 4], [3, 4, 4], [4, 5, 3], [4, 6, 1], [5, 6, 1]], [1, 3], 	[5])

import sys
import heapq

find = []

def solution(n, paths, gates, summits):
    INF = int(10e9)
    graph = [[] for i in range(n+1)]
    gates = set(gates)
    summits = set(summits)
    
    for a, b, c in paths:
        if a in gates or b in summits:
            graph[a].append((b, c))
        elif b in gates or a in summits:
            graph[b].append((a, c))
        else:
            graph[a].append((b, c))
            graph[b].append((a, c))
            
    inten = [INF] * (n+1)
    print(graph)
    
    def dix(start):
        q = []
        heapq.heappush(q, (0, start))

        while q:
            dist, now = heapq.heappop(q)
            print(dist, now)
            if inten[now] < dist: continue


            for i in graph[now]:
                if max(dist, i[1]) < inten[i[0]]:
                    inten[i[0]] = max(dist, i[1])
                    heapq.heappush(q, (max(dist, i[1]), i[0]))
    for i in gates:
        dix(i)
    print(inten)
    return find
solution(6, [[1, 2, 3], [2, 3, 5], [2, 4, 2], [2, 5, 4], [3, 4, 4], [4, 5, 3], [4, 6, 1], [5, 6, 1]], [1, 3], [5])