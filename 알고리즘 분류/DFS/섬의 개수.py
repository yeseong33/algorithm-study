import sys
sys.setrecursionlimit(10 ** 9)

d = [(1, 0), (0, 1), (-1, 0), (0, -1), (1, 1), (1, -1), (-1, 1), (-1, -1)]

def solution():
    global board, visited, d, n, m
    count = 0
    board = []
    for i in range(n):
        k = list(map(int, sys.stdin.readline().split()))
        board.append(k)
    visited = [[0]*m for _ in range(n)]
    
    for i in range(n):
        for j in range(m):
            if board[i][j] == 1 and not visited[i][j]:
                count += 1
                dfs(i, j)
    return count
    
def dfs(x, y):
    # solution 함수 밖에서 정의 되어 있기 때문에 solution 함수 내에서
    # 생기는 변수를 직접 참조 하지 못함 -> solution 함수에서 전역 변수를
    # 선언하고 난 뒤에 그 변수를 이용
    
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
    m, n = map(int, input().split())
    if n == 0 and m == 0:
        break
    count = solution()
    print(count)