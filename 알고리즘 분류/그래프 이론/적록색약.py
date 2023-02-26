import sys
from collections import deque

n = int(input())

paint = []
for i in range(n):
    s = sys.stdin.readline().strip()
    k = []
    for j in s:
        k.append(j)
    paint.append(k)

    
q = deque()
d = [(1, 0), (-1, 0), (0, 1), (0, -1)]
def bfs(x, y):
    q.append((x, y))
    
    visited[x][y] = 1
    
    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = x + d[i][0]
            ny = y + d[i][1]
            
            if 0 <= nx < n  and 0 <= ny < n and not visited[nx][ny]:
                if paint[x][y] == paint[nx][ny]:
                    visited[nx][ny] = 1
                    q.append((nx, ny))
                
cor1 = 0
cor2 = 0

visited = [[0] * n for i in range(n)]

for i in range(n):
    for j in range(n):
        if not visited[i][j]:
            bfs(i, j)
            cor1 += 1
            
            
visited = [[0] * n for i in range(n)]

for i in range(n):
    for j in range(n):
        if paint[i][j] == 'G':
            paint[i][j] = 'R'  


for i in range(n):
    for j in range(n):
        if not visited[i][j]:
            bfs(i, j)
            cor2 += 1

print(cor1, cor2)