import sys
input = sys.stdin.readline

n, m = map(int, input().split())
board = []
for i in range(n):
    k = list(map(int, input().split()))
    board.append(k)
    
visitd = [[0] * m for i in range(n)]    
dr = [(1, 0), (0, 1), (-1, 0), (0, -1)]
vir = []
for i in range(n):
    for j in range(m):
        if board[i][j]:
            if board[i][j] == 2:
                vir.append([i,j])         
            visitd[i][j] =1 

max_c = 0

def solution(board, vir):
    
    def dfs(d):
        global max_c
        if d == 3:
            c = bfs()
            if c > max_c:
                max_c = c 
            return
        
        for i in range(n):
            for j in range(m):
                if board[i][j] == 0:
                    if not visitd[i][j]:
                        board[i][j] = 1
                        visitd[i][j] = 1
                        dfs(d+1)
                        board[i][j] = 0
                        visitd[i][j] = 0
                        
    
    def bfs():
        visited_c = [i[:] for i in visitd]
        q = vir.copy()    
        while q:
            x, y = q.pop()
            if board[x][y] != 2 and visited_c[x][y]: continue
            visited_c[x][y] = 1
            for i in range(4):
                nx = x + dr[i][0]
                ny = y + dr[i][1]
                if 0<= nx < n and 0 <= ny < m:
                    if visited_c[nx][ny] == 0:
                        q.append([nx, ny])
        count = 0
        for i in range(n):
            for j in range(m):
                if visited_c[i][j] == 0:
                    count += 1 
        return count
    dfs(0)
    print(max_c)
    return

solution(board, vir)