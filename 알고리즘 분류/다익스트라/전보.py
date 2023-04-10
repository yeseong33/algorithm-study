# 이코테
import sys, heapq
INF = int(1e9)
n, m, c = map(int, sys.stdin.readline().split())


graph = [[] for _ in range(n+1)]
for _ in range(m):
    x, y, z = map(int, sys.stdin.readline().split())
    graph[x].append((y, z))
print(graph)
# 입력
# 3 2 1
# 1 2 4
# 1 3 2

start = c

# 도시까지 걸린 시간
city = [INF] * 30001

def dix(start):
    # 시작 위치를 기준으로 초기화
    q = []
    heapq.heappush(q, (0, start))
    city[start] = 0
    
    # 메세지를 받은 도시개수를 셈
    count = 0


    while q:
        print(q)
        time, now = heapq.heappop(q)
        
        if time > city[now]:
            continue
        
        for i in graph[now]:
            cost = city[now] + i[1]
            if city[i[0]] > cost:
                city[i[0]] = cost
                heapq.heappush(q, (cost, i[0]))
                count += 1
    return count


count = dix(start)
ma = 0
for i in city:
    if i != INF:
        ma = max(ma, i)
print(count ,ma)  

            



