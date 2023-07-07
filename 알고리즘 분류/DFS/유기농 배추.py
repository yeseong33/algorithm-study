import sys
sys.setrecursionlimit(10 ** 9)

t = int(input())


def dfs(x, y, c):
    
    
    visited[x][y] = c

    for k in range(4):
        nx = x + d[k][0] 
        ny = y + d[k][1]
        
        if 0 <= nx < n and 0 <= ny < m:
            if not visited[nx][ny] and board[nx][ny]:
                dfs(nx, ny, c)
                    


for _ in range(t):

    n, m, k = map(int, sys.stdin.readline().split())

    board = [[0] * m for i in range(n)]


    for i in range(k):
        a, b = map(int, sys.stdin.readline().split())
        board[a][b] = 1

        
    visited = [[0] * m for i in range(n)]

    d = [(1, 0), (-1, 0), (0, 1), (0, -1)]


    c = 0
    for i in range(n):
        for j in range(m):
            if board[i][j] == 1 and not visited[i][j]:
                c += 1
                dfs(i, j, c)

    print(c)
                            