import sys
# 플로이드 워셜 알고리즘
# 모든 노드에서 다른 모든 노들까지 최단 거리 계산
# 각 단계마다 특정한 노드 k를 거쳐 가는 경우를 확인
# 시간복잡도: O(N**3) -> n이 작을 때만 사용 가능
INF = int(1e9) # 10억

n = int(input())
m = int(input())

# 2차원 리스트로 그래프를 만들고 무한으로 초기화
graph = [[INF] * (n+1) for i in range(n+1)]

# 자기 자신에서 자기 자신으로 가는 비용을 0으로 초기화 
for i in range(1, n+1):
    for j in range(1, n+1):
        if i == j:
            graph[i][j] = 0

# 각 간선에 대한 정보를 입력 받아, 그 값으로 초기화
for _ in range(m):
    a, b, c = map(int, sys.stdin.readline().split())
    if c < graph[a][b]:
        graph[a][b] = c

# 점화식에 따라 플로이드 워셜 알고리즘 수행
for k in range(1, n+1):
    for i in range(1, n+1):
        for j in range(1, n+1):
            graph[i][j] = min(graph[i][j], graph[i][k] + graph[k][j])

# 수행된 결과 출력


# 다익스트라 알고리즘
# 특정 노드에서 출발해, 다른 모든 노드로 가는 최단 경로 계산
# 음의 간선이 없을 경우 정상적으로 작동
# 매 상황에서 가장 비용이 적은 노드 선택
# 시간 복잡도: O(ElogV)

import heapq
INF = int(1e9)

# 노드의 개수, 간선의 개수 받기
n, m = map(int, sys.stdin.readline().split())

# 시작 노드 번호를 입력받기
start = int(input())

# 각 노드에 연결되어 있는 노드에 대한 정보를 담는 리스트를 만들기
graph = [[] for i in range(n+1)]

# 최단 거리 테이블 모두 무한으로 초기화
distance = [INF] * (n+1)

# 모든 간선 정보를 입력받기
for _ in range(m):
    a, b, c = map(int, sys.stdin.readline().split())
    graph[a].append([b, c])
    
def dijkstra(start):
    q = []
    heapq.heappush(q, (0, start))
    distance[start] = 0
    while q: 
        dis, now = heapq.heappop(q)
        
        if distance[now] < dis:
            continue
        
        for i in graph[now]:
            cost = dis + i[1]
            if distance[i[0]] > cost:
                distance[i[0]] = cost
                heapq.heappush(q, (cost, i[0]))


# 최소 신장 트리, 크루스칼 알고리즘
# 신장트리: 그래프에서 모든 노드를 포함하며, 사이클이 존재하지 않는 
# 부분 그래프
# 시간 복잡도: O(ElogE)

# 특정 원소가 속한 집합 찾기
def find_parent(parent, x):
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])
    return parent[x]

# 두 원소가 속합 집합을 합치기
def union_parent(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)
    
    if a < b:
        parent[b] = a
    else:
        parent[a] = b 
        
# 노드의 개수와 간선의 개수 입력 받기
v, e = map(int, sys.stdin.readline().split())
parent = [0] * (v+1)

# 모든 간선을 담을 리스트와, 최종 비용을 담을 변수
edges = []
result = 0

# 부모 테이블상에서, 부모를 자기 자신으로 초기화
for i in range(1, v+1):
    parent[i] = i
    
# 모든 간선 정보 입력 받기
for _ in range(e):
    a, b, cost = map(int, sys.stdin.readline().split())
    edges.append((cost, a, b))
    
# 간선을 비용순으로 정렬
edges.sort()

# 간선을 하나씩 확인
for edge in edges:
    cost, a, b = edge
    if find_parent(parent, a ) != find_parent(parent, b):
        union_parent(parent, a, b)
        result += cost


# 위상 정렬
# 사이클이 없는 방향 그래프의 모든 노드를 방향성에 거스르지 않도록 
# 순서대로 나열
# 그래프는 사이클이 없는 방향 그래프이어야 함
# 모든 원소를 방문하기 전에 큐가 빈다면 사이클이 존재한다고 판단
# 시간 복잡도: O(V+E)
from collections import deque

# 노드의 개수와 간선의 개수를 입력 받기
v, e = map(int, sys.stdin.readline().split())

# 모든 노드에 대한 진입차수는 0으로 초기화
indegree = [0] * (v+1)

# 각 노드에 연결된 간선 정보를 담기 위한 연결 리스트 초기화
graph = [[] for i in range(v+1)]

# 방향 그래프의 모든 간선 정보를 입력 받기
for _ in range(e):
    a, b = map(int, sys.stdin.readline().split())
    graph[a].append(b)
    # 진입차수 1 증가
    indegree[b] +=1
    
# 위상 정렬
def topology_sort():
    result = []
    q = deque()
    # 처음 시작시 진입차수가 0인 노드 삽입
    for i in range(1, v+1):
        if indegree[i] == 0:
            q.append(i)
    while q:
        now = q.popleft()
        result.append(now)
        # 해당 원소와 연결되어 있는 모든 노드의 진입차수 1 빼기
        for i in graph[now]:
            indegree[i] -= 1
            
            if indegree[i] == 0:
                q.append(i)
    
    for i in result:
        print(*i)
        