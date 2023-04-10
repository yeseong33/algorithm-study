import sys, heapq
INF = int(1e9) # 10억을 최대로 지정

# 값을 받음
n = int(input())
m = int(input())

# 그래프
graph = [[] for _ in range(n+1)]

# 그래프에 값 할당
for i in range(m):
    a, b, c = map(int, sys.stdin.readline().split()) 
    graph[a].append((b, c))
    
# 출발지점에서 다른 지점까지의 거리를 저장할 리스트
distance = [INF] * (n+1)

def diex(start):
    # 초기화
    distance[start] = 0
    
    # 현재위치에서 가장 거리가 짧은 노드를 구하기 위한 우선순위 큐 
    q = []
    heapq.heappush(q, (0, start))
    
    # 큐가 빌 때 까지 돌림
    while q:
        dist, now = heapq.heappop(q)
        
        # 이미 가장 최소의 값이면 넘어감
        # visited의 기능을 함
        if dist > distance[now]:
            continue
        
        for i in graph[now]:
            cost = distance[now] + i[1]
            
            # 현재노드에서 다음 노드까지의 값이
            # 다음노드의 값보다 작으면 갱신
            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(q, (cost, i[0]))
                
    
start, end = map(int, sys.stdin.readline().split())

diex(start)

print(distance[end])    
    