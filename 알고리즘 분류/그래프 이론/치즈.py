import sys
from collections import deque

# 공기 9, 치즈 1, 치즈안  2
n, m = map(int, sys.stdin.readline().split())


chez = []
visited = []
d = [(1,0), (-1,0), (0,1), (0,-1)]
for i in range(n):
    k = list(map(int, sys.stdin.readline().split()))
    chez.append(k)
    


# for i in range(n):
#     for j in range(m):
#         if chez[i][j] == 1:
#             cc += 1


## 외부 공기 찾기
air = deque()

for i in range(n):
    if 0 < i < n-1:
        continue 
    for j in range(m):
        if chez[i][j] == 0 or chez[i][j] == 9:
            air.append((i, j))

visited = [[0] * m for i in range(n)]


def bfs():
    global d
    
    while air:
        # print(air)
        x, y = air.popleft()
        visited[x][y] = 1
        for i in range(4):
            nx=  x + d[i][0]
            ny = y + d[i][1]
            
            if 0 <= nx < n and 0 <= ny < m and (chez[nx][ny] == 0):
                if not visited[nx][ny]: 
                    chez[nx][ny] = 9
                    air.append((nx, ny))
     
# 외부공간, 치즈 나누기            
bfs()
# 치즈 개수 찾기, 치즈 위치 입력
chez_count = 0

for i in range(n):
    for j in range(m):
        if chez[i][j] == 1:
            chez_count +=1 

time = 0 
while chez_count > 0 :
    print(chez_count)
    time += 1
    chez_temp = [item[:] for item in chez]

    for i in range(n):
        for j in range(m):
            if chez[i][j] == 1:
                ex =0 
                for k in range(4):
                    ni = i + d[k][0]
                    nj = j + d[k][1]
                    
                    if chez[ni][nj] == 9:
                        ex += 1
                if ex > 1:
                    chez_temp[ni][nj] = 9
                    chez_count -= 1
                    
    chez = [item[:] for item in chez_temp]
    
    air = deque()

    for i in range(n):
        if 0 < i < n-1:
            continue 
        for j in range(m):
            if chez[i][j] == 0 or chez[i][j] == 9:
                air.append((i, j))
    
    visited = [[0] * m for i in range(n)]
    bfs()
    for i in chez:
        print(i)
print(time)

# 0 0 0 0 0 0 0 0 0
# 0 0 0 0 0 0 0 0 0
# 0 0 0 0 0 0 0 0 0
# 0 0 0 0 1 0 0 0 0
# 0 0 0 0 1 0 0 0 0
# 0 0 0 0 0 0 0 0 0
# 0 0 0 0 0 0 0 0 0
# 0 0 0 0 0 0 0 0 0