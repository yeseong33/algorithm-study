import sys
from collections import deque


m, n, H = map(int,sys.stdin.readline().split())

box = []
visited = []
for _ in range(H):
    k = [list(map(int, sys.stdin.readline().split())) for i in range(n)]
    a = [[0] * m for i in range(n)]
    box.append(k)
    visited.append(a)


q = deque()
day = -1
tomato = 0
newmato = 0

for i in range(H):
    for j in range(n):
        for k in range(m):
            
            if box[i][j][k] == 1:
                tomato += 1 
                visited[i][j][k] = 1
                q.append((i, j, k))
            if box[i][j][k] == -1:
                visited[i][j][k] = 1


def bfs(q):
    global day, tomato, newmato
    
    D = [(1, 0), (-1, 0), (0, 1), (0, -1)]
    d = [1, -1]
    
    while q:
        h, x, y = q.popleft()
        tomato -= 1
        
        # 수평 방향에 대해
        for i in range(4):
            nx = x + D[i][0]
            ny = y + D[i][1]
            if  0 <= nx < n and 0 <= ny < m: 
                if not visited[h][nx][ny] :
                    visited[h][nx][ny] = 1
                    q.append((h, nx, ny))
                    newmato += 1
            
        # 수직 방향에 대해
        for i in range(2):
            nh = h + d[i]
            
            if 0 <= nh < H and not visited[nh][x][y] : 
                visited[nh][x][y] = 1
                q.append((nh, x, y))
                newmato += 1

        if tomato == 0:
            day += 1
            tomato = newmato
            newmato = 0
    for i in range(H):
        for j in range(n):
            for k in range(m):
                if visited[i][j][k] == 0:
                    day = -1
                    return
bfs(q)

print(day)
