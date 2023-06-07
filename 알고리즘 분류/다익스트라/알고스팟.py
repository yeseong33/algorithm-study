import sys
from collections import deque


m, n = map(int, sys.stdin.readline().split())

maze = []

for i in range(n):
    k = list(map(int, sys.stdin.readline().strip()))
    maze.append(k)

    
d = [(1, 0), (0, 1), (-1, 0), (0, -1)]

def dk(x, y):
    q = deque()
    q.append((x, y))
    
    visited = [[0] * m for _ in range(n)]
    visited[x][y] = 1
    
    while q:
        x, y = q.popleft()
        
        for i in range(4):
            nx = x + d[i][0]
            ny = y + d[i][1]
            
            if 0 <= nx <= n-1 and 0 <= ny <= m-1:
                if nx == n-1 and ny == m-1:
                    return visited[x][y]
                
                if visited[nx][ny] == 0:
                    if maze[nx][ny] == 0: 
                        visited[nx][ny] = visited[x][y]
                        q.appendleft((nx, ny))
                    elif maze[nx][ny] == 1:
                        visited[nx][ny] = visited[x][y]+1
                        q.append((nx, ny))

if m == 1 and n == 1:
    print(0)
else:
    s = dk(0, 0)
    print(s-1)
