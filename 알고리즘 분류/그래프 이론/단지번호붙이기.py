import sys
from collections import deque
n = int(input())

board = []

for i in range(n):
    k = list(map(int, sys.stdin.readline().strip()))
    board.append(k)

visited = [[0] * n for _ in range(n)]
d = [(1, 0), (0, 1), (-1, 0), (0, -1)]

def BFS(a, b,dan):
    q = deque()
    q.append([a, b])
    board[a][b] = dan
    
    while q:
        x, y = q.popleft()
        
        for i in range(4):
            nx = x + d[i][0] 
            ny = y + d[i][1]
            
            if 0 <= nx < n and 0 <= ny < n:
                if board[nx][ny] == 1:
                      board[nx][ny] = dan
                      q.append([nx, ny])
    
    
dan = 2
for i in range(n):
    for j in range(n):
        if board[i][j] == 1:
            BFS(i, j, dan)
            dan += 1

k = dan - 2
t = [0] * (k + 2)

for i in range(n):
    for j in range(n):
        if board[i][j] != 0:
            t[board[i][j]] += 1
print(k)
t.sort()
for i in t[2:]:
    print(i)