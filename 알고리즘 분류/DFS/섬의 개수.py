import sys
sys.setrecursionlimit(10 ** 9)

d = [(1, 0), (0, 1), (-1, 0), (0, -1), (1, 1), (1, -1), (-1, 1), (-1, -1)]
n = 0
m = 0
board = []
visited = []

def solution(a, b):
    global board, visited, d, n, m
    n = a
    m = b 
    count = 0
    board_t = []
    for i in range(n):
        k = list(map(int, sys.stdin.readline().split()))
        board_t.append(k)
    visited_t = [[0]*m for _ in range(n)]
    board = board_t    
    visited = visited_t    
    
    for i in range(n):
        for j in range(m):
            if board[i][j] == 1 and not visited[i][j]:
                count += 1
                dfs(i, j)
    return count
    
def dfs(x, y):
    global board, visited, d, n, m 
    # 범위에 벗어나거나, 방문된적 있거나, 바다라면 리턴
    if not (0 <= x < n and 0 <= y < m) or visited[x][y] or board[x][y] == 0: 
        return
    visited[x][y] = 1
    
    # 8방향 탐색
    for i in range(8):
        nx = x + d[i][0]    
        ny = y + d[i][1]
        dfs(nx, ny)
        
while True:
    a, b = map(int, input().split())
    if a == 0 and b == 0:
        break
    count = solution(b, a)
    print(count)