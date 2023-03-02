import sys
sys.setrecursionlimit(10 ** 5)

n ,m = map(int, sys.stdin.readline().split())

maze = [[0] * (m+1)]

for i in range(n):
    k = [0] + list(map(int, sys.stdin.readline().split()))
    maze.append(k)
    
visited = [[-1] * (m+1) for i in range(n+1)]

dir = [(1, 0), (0, 1), (1, 1)]

def dp(x, y):
    
    if x == n and y == m:
        visited[x][y] = maze[x][y]
        return
    
    if visited[x][y] != -1:
        return
    
    for i in range(3):
        nx = x + dir[i][0]
        ny = y + dir[i][1]

        
        if 1 <= nx <= n and 1 <= ny <= m:
            
                dp(nx, ny)
                visited[x][y] = max(visited[x][y], maze[x][y]+ visited[nx][ny])
                
dp(1, 1)
print(visited[1][1])
