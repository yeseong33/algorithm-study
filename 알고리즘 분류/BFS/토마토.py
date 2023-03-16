import sys
from collections import deque

m, n = map(int, sys.stdin.readline().split())

box = []
visited = [[0] * m for i in range(n)]
d = [(1, 0), (-1, 0), (0, 1), (0, -1)]
for i in range(n):
    box.append(list(map(int, sys.stdin.readline().split())))

start = []

for i in range(n):
    for j in range(m):
        if box[i][j] == 1:
            visited[i][j] = 1
            start.append((i, j))
        elif box[i][j] == -1:
            visited[i][j] = -1

def BFS(tomatos):
    
    
    q = deque(tomatos)
    day = 0 
    c = len(q)
    while q:
        
        if c == 0:
            c = len(q)
            day += 1
        
        x, y = q.popleft()
        c-=1
        for i in range(4):
            nx = x + d[i][0]
            ny = y + d[i][1]
            
            if 0 <= nx < n and 0 <= ny < m:
                if not visited[nx][ny]:
                    visited[nx][ny] = 1
                    q.append((nx, ny))
    return day

day = BFS(start)

for i in range(n):
    for j in range(m):
        if visited[i][j] == 0:
            day = -1
            break
    if day == -1: 
        break

if day == -1:
    print(-1)
else:
    print(day)
        
        