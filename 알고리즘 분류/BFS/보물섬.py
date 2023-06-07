import sys
from collections import deque

n, m = map(int, sys.stdin.readline().split())

Map = []

for i in range(n):
    k = list(sys.stdin.readline().strip())
    Map.append(k)    


d = [(1, 0), (0, 1), (-1, 0), (0, -1)]


def bfs(sx, sy):
    visited = [[0] * m for i in range(n)]
    q = deque()
    visited[sx][sy] = 1
    q.append((sx, sy))
    m_c = 0
    while q:
        x, y  = q.popleft()
        
        for i in range(4):
            nx = x + d[i][0]
            ny = y + d[i][1]
            
            if 0 <= nx <= n-1 and 0 <= ny <= m-1:
                if visited[nx][ny] == 0 and Map[nx][ny] == 'L':
                    visited[nx][ny] = visited[x][y]+ 1
                    q.append((nx, ny))
                    m_c = max(m_c, visited[nx][ny])
    return m_c-1


tet = 0

for i in range(n):
    for j in range(m):
        tet = max(tet, bfs(i, j) )
print(tet)             
                    
                    
            
    
    