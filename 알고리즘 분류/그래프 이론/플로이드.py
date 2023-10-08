import sys
INF = int(10e9)
n = int(sys.stdin.readline().strip())
m = int(sys.stdin.readline().strip())

city = [[INF] * (n+1) for i in range(n+1)]

for i in range(m):
    a, b, c = list(map(int, sys.stdin.readline().split()))
    city[a][b] = min(c, city[a][b])
    

for i in range(1, n+1): 
    for j in range(1, n+1):
        if i == j:
            city[i][j] = 0
            
def flo():
    
    for k in range(1, n+1):
        for i in range(1, n+1):
            for j in range(1, n+1):
                city[i][j] = min(city[i][j], city[i][k] + city[k][j]) 
    
    for i in range(1, n+1):
        for j in range(1, n+1):
            if city[i][j] == INF:
                city[i][j] = 0
    
    for row in city[1:]:
        for col in row[1:]:
            if col == 100001:
                print(0, end = " ")
            else:
                print(col, end = " ")
        print()
flo()

# #입력
# n = int(input())
# m = int(input())
# bus_cost = [[100001 for _ in range(n+1)] for _ in range(n+1)]

# for _ in range(m):
#     start, end, cost = map(int, input().split())
#     bus_cost[start][end] = min(cost, bus_cost[start][end])

# #플로이드-워셜 알고리즘
# for k in range(1, n+1): #경로 for문이 가장 상위 단계여야 누락되지 않는다
#     for i in range(1, n+1):
#         for j in range(1, n+1):
#             if i == j: #자기 자신으로 오는 경우는 없다고 했으므로
#                 bus_cost[i][j] = 0 
#             else: #경로 거치는 것 or 직접 가는 것 or 이전 경로들
#                 bus_cost[i][j] = min(bus_cost[i][j],
#                                      bus_cost[i][k] + bus_cost[k][j])


# #출력
# for row in bus_cost[1:]:
#     for col in row[1:]:
#         if col == 100001:
#             print(0, end = " ")
#         else:
#             print(col, end = " ")
#     print()