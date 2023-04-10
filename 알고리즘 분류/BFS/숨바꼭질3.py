# import sys
# from collections import deque
# INF = int(1e9)

# # 위치값
# n, k = map(int, sys.stdin.readline().split())

# # 위치까지의 값 저장
# find = [-1] * 100001
# visited = [False] * 100001  

# def bfs(start):
#     q = deque()
#     q.append(start)
#     visited[start] = True
#     find[start] = 0
    
#     while q:
#         now = q.popleft()
        
#         if now * 2 <= 100001 and not visited[now * 2]:
#             q.append(now * 2)
#             visited[now * 2] = True
#             find[now * 2] = find[now]
            
#         if now + 1 <= 100001 and not visited[now+1]:
#             q.append(now+1)
#             visited[now+1] = True
#             find[now+1] = find[now] + 1
            
#         if now - 1 <= 100001 and not visited[now-1]:
#             q.append(now-1)
#             visited[now-1] = True
#             find[now-1] = find[now] + 1

# bfs(n)
# print(find[k])

# 다익스트라로 문제 풀이
import sys, heapq
from collections import deque
INF = int(1e9)

# 위치값
n, k = map(int, sys.stdin.readline().split())

# 위치까지의 값 저장
find = [INF] * 100001

# 다익스트라 구현
def dix(start):
    q = []
    heapq.heappush(q, (0, start))
    find[start] = 0
    
    while q:
        value, node = heapq.heappop(q)

        for next_node in [node+1, node-1, node * 2]:
            if 0 <= next_node <= 100000:
                if next_node == node * 2 and find[next_node] == INF:
                    find[next_node] = value
                    heapq.heappush(q, (value, next_node))
                elif find[next_node] == INF:
                    find[next_node] = value +1
                    heapq.heappush(q, (value+1, next_node))
                
            
dix(n)

if n <= k:
    print(find[k])
else:
    print(n-k)
    
            