import sys, heapq
INF = int(1e9)
n, m, x = map(int, sys.stdin.readline().split())

# graph 만들기
graph = [[] for _ in range(n+1)]

for _ in range(m):
    a, b, c = map(int, sys.stdin.readline().split())
    graph[a].append((b,c))

def dix(start):
    q = []
    heapq.heappush(q, (0, start))
    # 시간을 기록할 테이블
    time = [INF] * (n+1) 
    # 초기화
    time[start] = 0
    
    while q:
        value, now = heapq.heappop(q)
        if value > time[now]:
            continue
        
        for i in graph[now]:
            cost = value + i[1]
            
            if cost < time[i[0]]:
                time[i[0]] = cost
                heapq.heappush(q, (cost, i[0]))
    return time


max_time = 0

for i in range(1, n+1):
    go = dix(i)
    back = dix(x)
    max_time = max(max_time, go[x] + back[i])
print(max_time)