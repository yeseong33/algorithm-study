# import sys
# INF = int(1e9) # 무한을 의미함 - 10억

# # 정점의 개수, 노드의 개수 받기
# v, e = map(int, sys.stdin.readline().split())

# # 시작점 받기
# start = int(input())
 

# # 그래프 그리기
# # 그래프 리스트
# graph = [[] for _ in range(v+1)]

# # 입력값을 받아 a에서 b까지의 가중치 c, 그래프로 만듦
# for i in range(e):
#     a, b, c = map(int, sys.stdin.readline().split())
#     graph[a].append((b, c))

# # 방문한 적 있는지 체크
# visited = [False] * (v+1)    

# # 최단거리 테이블 생성
# distance = [INF] * (v+1)

# # 방문하지 않은 노드 중, 최단거리가 가장 짧은 노드의 번호를 반환
# def get_smallest_node():
#     min_value = INF
#     idx = 0
#     for i in range(1, v+1):
#         if distance[i] < min_value and not visited[i]:
#             min_value = distance[i]
#             idx = i
#     return idx
        
# # 다익스트라 구현
# def diex(start):
#     # 시작 노드에 대해서 초기화
#     distance[start] = 0
#     visited[start] = True
    
#     for t in graph[start]:
#         distance[t[0]] = t[1]
    
#     for i in range(v-1):
#         now = get_smallest_node()
#         visited[now] = True
        
#         # 현재 노드와 연결된 다른 노드 확인
#         for j in graph[now]:
#             cost = distance[now] + j[1]
#             if cost < distance[j[0]]:
#                 distance[j[0]] = cost

# diex(start)

# for i in range(1, v+1):
#     if distance[i] == INF:
#         print('INF')
#     else:
#         print(distance[i])
    

# heap 자료구조를 이용해 구현
import sys, heapq
INF = int(1e9) # 무한을 의미함 - 10억

# 정점의 개수, 노드의 개수 받기
v, e = map(int, sys.stdin.readline().split())

# 시작점 받기
start = int(input())

# 그래프 그리기
# 그래프 리스트
graph = [[] for _ in range(v+1)]

# 입력값을 받아 a에서 b까지의 가중치 c, 그래프로 만듦
for i in range(e):
    a, b, c = map(int, sys.stdin.readline().split())
    graph[a].append((b, c))

# 방문한 적 있는지 체크
visited = [False] * (v+1)    

# 최단거리 테이블 생성
distance = [INF] * (v+1)


def diex(start):
    # 힙 생성
    q = []
    
    heapq.heappush(q, (0, start))
    distance[start] = 0
    
    while q:
        # 거리가 가장 짧은 노드 정보 꺼냄
        # 우선순위 큐를 사용하기 때문에, 값이 작은
        # 즉, 거리 값이 가장 짧은 노드 먼저 pop하게 된다.
        dist, now = heapq.heappop(q)
        
        # 이미 최소의 경로를 구했다면 넘어감
        if distance[now] < dist:
            continue
        
        # 현재 노드와 연결된 노드의 거리들을 갱신
        for i in graph[now]:
            cost = distance[now] + i[1]
            # 만약 연결된 노드의 값보다 현 노드를 통해 가는 값이 
            # 더 작다면, 값 갱신 및 갱신된 노드 힙에 추가
            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(q, (distance[i[0]], i[0]))

diex(start)

for i in range(1, v+1):
    if distance[i] == INF:
        print("INF")
    else:
        print(distance[i])
        
    