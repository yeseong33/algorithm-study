import sys

n, m = map(int, sys.stdin.readline().split())

maze = [[0] *(m+1)]
for i in range(n):
    k = [0] + list(map(int, sys.stdin.readline().split()))
    maze.append(k)
    
ans = [[0] * (m+1) for i in range(n+1)]
D = [(1, 0), (0, 1), (1, 1)] 

def dp(maze, ans, x, y):
    
    if x == n and y == m:
        ans[n][m] = maze[n][m]
        return 
    
    
    for dx, dy in D:
        nx = x + dx
        ny = y + dy
        
        if 1 <= nx <= n and 1 <= ny <= m:
            dp(maze, ans, nx, ny)
            ans[x][y] += maze[nx][ny]
    
    
dp(maze, ans , 1, 1)
print(ans[1, ])