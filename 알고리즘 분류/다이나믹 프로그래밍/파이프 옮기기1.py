import sys

n = int(input())

board = [[0] * (n+1)]

for i in range(n):
    k = [0] + list(map(int, sys.stdin.readline().split()))
    board.append(k)
# 
    
# visited = [[[-1, [0, 0, 0, 0]] for i in range(n+1) ] for i in range(n+1)]

d = [0, [1, 3], [2, 3], [1, 2, 3]]
count = 0 
def dfs(x, y, p):
    global count

    if x == n and y == n:
        count += 1
        return

    if p == 1 or p == 3:
        if y +1 < n+1  and board[x][y+1] == 0:
            dfs(x, y+1, 1) 
    if p == 2 or p == 3:
        if x + 1 < n+1 and board[x+1][y] == 0:
            dfs(x+1, y, 2)
    
    if x+1 < n+1 and y+1 < n+1:
        if board[x+1][y] == 0 and board[x][y+1] == 0 and board[x+1][y+1] == 0:
            dfs(x+1, y+1, 3) 


    
# 가로 - 1, 세로 - 2, 대각선 - 3

def move(dir, x, y):
    if dir == 1:
        nx = x
        ny = y + 1
        if 1 <= nx < n+1 and 1 <= ny < n+1 and board[nx][ny] != 1:
            return nx, ny
    elif dir == 2:
        nx = x + 1
        ny = y
        if 1 <= nx < n+1 and 1 <= ny < n+1 and board[nx][ny] != 1:
            return nx, ny
    elif dir == 3:
        nx = x + 1
        ny = y + 1
        if 1 <= nx < n+1 and 1 <= ny < n+1 and board[nx][ny] != 1 and board[nx-1][ny] != 1 and board[nx][ny-1] != 1:
            return nx, ny
    return 0, 0
            

if board[n][n] == 1:
    print(count)
else: 
    dfs(1, 2, 1)
    print(count)

