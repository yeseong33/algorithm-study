# dfs, 빙산 기준
import sys
from collections import deque
sys.setrecursionlimit(10 ** 5)
n, m = map(int, sys.stdin.readline().split()) 

arctic = []
d = [(1, 0), (-1, 0), (0, 1), (0, -1)]

for i in range(n):
    k = list(map(int, sys.stdin.readline().split()))
    arctic.append(k)

def melting(x, y):
    
    for i in range(4):
        nx = x + d[i][0]
        ny = y + d[i][1]
        
        if 0 <= nx < n and 0 <= ny < m:
            if not arctic[nx][ny]:
                arctic[x][y] -= 1

def dfs(x, y):

    visited[x][y] = 1
    
    for i in range(4):
        nx = x + d[i][0]
        ny = y + d[i][1]
        
        if 0 <= nx < n and 0 <= ny <m and not visited[nx][ny] and arctic[nx][ny]:
            dfs(nx, ny)
        
time = 0 
count = 0 
start = True
visited = [[0] * m for i in range(n)]

for i in range(n):
        for j in range(m):
            if arctic[i][j] and not visited[i][j]:
                count += 1
                   
                dfs(i, j) 
if count > 1:
    start = False


while start:
    time +=1 
    

    for i in range(n):
        for j in range(m):
            if arctic[i][j]:
                melting(i,j)
                if arctic[i][j] < 0:
                    arctic[i][j] = 0
    
    count = 0 
    visited = [[0] * m for i in range(n)]
        
    for i in range(n):
        for j in range(m):

            if arctic[i][j] and not visited[i][j]:
                count += 1
                if count == 2:
                    break
                dfs(i, j) 
    
    if count >1:
        break

    s = 0
    for i in range(n):
        for j in range(m):
            s += arctic[i][j]
    if s == 0:
        break

if count >  1:
    print(0)
else:
    print(time)

# [[0, 0, 0, 0, 0, 0, 0],
#  [0, 2, 4, 5, 3, 0, 0],
#  [0, 3, 0, 2, 5, 2, 0], 
#  [0, 7, 6, 2, 4, 0, 0],
#  [0, 0, 0, 0, 0, 0, 0]]