import sys

n, m, h = map(int, sys.stdin.readline().split())
if m == 0: # M이 0일 경우 출발점에서 도착점으로 바로 내려오므로 0 출력 후 종료
    print(0)
else:
    board = [[0] * (n)for _ in range(h)]

    for i in range(m):
        a, b = map(int, sys.stdin.readline().split())
        board[a-1][b-1] = 1
        
    def check(board):
        for i in range(n):
            now = i
            for j in range(h):
                if board[j][i] == 1:
                    i += 1
                elif i != 0 and board[j][i-1]:
                    i -= 1
                j += 1
            if i != now:
                return False
        return True
                    
    min_ladder = 4

    def dfs(board, count, a, b):
        global min_ladder 
        
        if check(board):
            if count < min_ladder:
                min_ladder = count
            return 
        
        elif count >= min_ladder or count == 3:
            return 

        for i in range(a, h):
            if i == a:
                start_y = b
            else:
                start_y = 0
            for j in range(start_y, n-1):
                if not board[i][j] and not board[i][j+1]:
                    if j > 0 and board[i][j - 1]: continue
                    board[i][j] = 1
                    dfs(board, count+1, i, j+2)
                    board[i][j] = 0
        
    dfs(board, 0, 0, 0)
    if min_ladder > 3:
        print(-1)
    else: 
        print(min_ladder)
        
    