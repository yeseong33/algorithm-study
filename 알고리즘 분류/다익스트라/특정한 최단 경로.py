import sys, heapq
INF = int(1e9)

n, e = map(int, sys.stdin.readline().split())

# graph 만들기
graph = [[] for _ in range(n+1)]

for i in range(e):
    a, b, c = map(int, sys.stdin.readline().split())
    graph[a].append((b, c))
    graph[b].append((a, c))
    
m1, m2 = map(int, sys.stdin.readline().split())

distance = [INF] * (n+1) 

def dix(start):
    q = []
    heapq.heappush(q, (0, start))
    
    distance = [INF] * (n+1) 
    distance[start] = 0
    
    while q:
        value, now = heapq.heappop(q)
        
        if distance[now] < value:
            continue
        
        for i in graph[now]:
            cost = value + i[1]
            
            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(q, (cost ,i[0]))
    
    return distance



second = dix(m1)
thrd = dix(m2)
last = dix(n)

result_1 = last[m2] + thrd[m1] + second[1]
# 고민 많이 함
result_2 = last[m1] + second[m2] + thrd[1]
result = min(result_1, result_2)

if result >= INF:
    print(-1)
else:
    print(result)