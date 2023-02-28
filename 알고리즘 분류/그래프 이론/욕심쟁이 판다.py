import sys
from collections import deque
sys.setrecursionlimit(10 **5)

n = int(input())

forest = []

for i in range(n):
    k = list(map(int, sys.stdin.readline().split()))
    forest.append(k)
d = [(1, 0), (-1, 0), (0, 1), (0, -1)]
    
q = deque()
visited = [[0] * n for _ in range(n)]

max_load = 0

def dfs(x, y):
    
    if visited[x][y]:
        return
    
    con = False
    
    for i in range(4):
        nx = x + d[i][0]
        ny = y + d[i][1]
        if 0 <= nx < n and 0 <= ny < n:
            if forest[x][y] < forest[nx][ny]:
                con = True
                dfs(nx, ny)
                visited[x][y] = max(visited[nx][ny]+1, visited[x][y])
        
                
    if not con:
        visited[x][y] = 1
        return


for i in range(n):
    for j in range(n):
        dfs(i, j)
        
max_l = 0 
for i in visited:
    k = max(i)
    if k > max_l:
        max_l = k
print(max_l)
