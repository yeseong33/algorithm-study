import sys
from collections import deque


n = int(input())

land = []

for i in range(n):
    k = list(map(int, sys.stdin.readline().split()) )
    land.append(k)


visited = [[0] * n for i in range(n)]

d = [(1, 0), (0, 1), (-1, 0), (0, -1)]
# 섬 구분
def split(x, y, c):
    
    q = deque()
    q.append((x, y))
    
    while q:
        x, y = q.popleft()

        for i in range(4):
            nx = x + d[i][0]
            ny = y + d[i][1]
            
            if 0 <= nx <= n-1 and 0 <= ny <= n-1:
                if visited[nx][ny] == 0 and land[nx][ny] == 1:
                    visited[nx][ny] = c
                    q.append((nx, ny))
                    
land_num = n * n + 1           
count = 0 
for i in range(n):
    for j in range(n):
        if land[i][j] == 1:
            if visited[i][j] == 0:
                visited[i][j] = land_num
                split(i, j, land_num)
                land_num += 1
                count +=1 


def makeB(v):
    
    dist = [[-1] * n for i in range(n)]
    q = deque()

    for i in range(n):
        for j in range(n):
            if visited[i][j] == v:
                dist[i][j] = 0
                q.append((i, j))    
    
    while q:
        x, y = q.popleft()

        for i in range(4):
            nx = x + d[i][0]
            ny = y + d[i][1]
            
            if 0 <= nx <= n-1 and 0 <= ny <= n-1:
                if dist[nx][ny] == -1 and visited[nx][ny] == 0:
                    dist[nx][ny] = dist[x][y] + 1
                    q.append((nx, ny))
                elif visited[nx][ny] != 0 and visited[nx][ny] != v:
                    return dist[x][y]                    
                
    
    return 99999999999999999
s = 9999999999999


for i in range(n*n+1, n*n+1 + count):
    s = min(s, makeB(i))

    
print(s)
            
            