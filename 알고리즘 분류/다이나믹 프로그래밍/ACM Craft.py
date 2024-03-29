# ## 직전에 필요한 애들  다른 애들이랑 연결 되어 있을 경우 --> 제거 후 다른 애들이랑 연결

# import sys
# from collections import deque
# t = int(input())



# for _ in range(t):
#     n, k = map(int, sys.stdin.readline().split())

#     cost = list(map(int ,sys.stdin.readline().split()))

#     bild = [[]  for i in range(n)]
#     print(bild)

#     for i in range(k):
#         b, nb = map(int, sys.stdin.readline().split())
#         bild[nb-1].append(b) 

#     goal = int(sys.stdin.readline())

#     must = bild[goal-1]
#     end = []
    
    
    
#     print(cost, 'cost')

#     time = [0] * (n + 1)

#     print(bild)

#     def bfs():
        
#         time[goal-1] = cost[goal-1]
        
#         queue = deque(bild[goal-1])
        

        
#         while queue:
#             v = queue.popleft()
#             print(v, 'v')
            
#             if bild[v-1]:
#                 for w in bild[v-1]:
#                     if time[w-1] < time[v-1] + cost[w-1]:
#                         time[w-1] = time[v-1] + cost[w-1]
#                         queue.append(w)
#             else:
#                 print(v, 'v')
#                 end.append(v)
    
                
#     bfs()
#     print(end, "end")
#     print(time,"t")
#     maxV = 0
#     for i in end:
#         if time[i-1] > maxV:
#             maxV = time[i-1]
#     print(max(time))

    
# # [[], [1], [2, 1], [3, 2, 1], [4, 3, 2, 1]]


# import sys
# from collections import deque
# t = int(input())

# def bfs(n):
    
#     need_visited = deque([n])
#     time[n] = cost[n-1]
    
#     while need_visited:
#         v = need_visited.popleft()
        
#         if bild[v]:
#             for i in bild[v]:
#                 if time[i] < time[v] + cost[i-1]:
#                     time[i] = time[v] + cost[i-1]
#                     need_visited.append(i)
        
#         else:
#             end.append(v)
            
# for _ in range(t):
#     n, k = map(int, sys.stdin.readline().split())

#     cost = list(map(int ,sys.stdin.readline().split()))

#     bild = [[]  for i in range(n+1)]

#     for i in range(k):
#         b, nb = map(int, sys.stdin.readline().split())
#         bild[nb].append(b) 

#     goal = int(sys.stdin.readline())
#     time = [0] * (n+1)

#     end = []

#     bfs(goal)
#     maxV = 0
#     for i in end:
#         if time[i] > maxV:
#             maxV = time[i]
#     print(maxV)
                        


import sys
sys.setrecursionlimit(10 ** 5)

t = int(input())


def dp(node):
    
    if takeTime[node] != -1:
        return
    
    if not graph[node]:
        takeTime[node] = times[node]
        return
    
    takeTime[node] = 0
    
    for i in graph[node]:
        dp(i)
        takeTime[node] = max(takeTime[i]+times[node], takeTime[node])

    
for i in range(t):
    n, k = map(int, sys.stdin.readline().split())
    times = [0] + list(map(int, sys.stdin.readline().split()))
    
    # 그래프 만들기
    graph = [[] for i in range(n+1)]
    for i in range(k):
        x, y =  map(int, sys.stdin.readline().split())
        graph[y].append(x)
        
    # 지어야 하는 건물 노드
    startNode = int(sys.stdin.readline().strip())

    # dp 돌리기 위한 초기화
    takeTime = [-1] * (n+1)
    
    # dp 돌리기
    dp(startNode)
    print(takeTime[startNode])


