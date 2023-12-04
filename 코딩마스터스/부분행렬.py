import sys
input = sys.stdin.readline

n, m, x = map(int, input().split())

board = [[0] * (m+1)] + [[0] + list(map(int, input().split())) for _ in range(n)]

for i in range(1, n+1):
    for j in range(1, m+1):
        board[i][j] +=  board[i-1][j] + board[i][j-1] - board[i-1][j-1]

def run():
    for i in range(1, n+1):
        for j in range(1, m+1):
            for a in range(i, n+1):
                for b in range(j, m+1):
                    now = board[a][b] - (board[a-i][b]+board[a][b-j]-board[a-i][b-j])
                    if now == x:
                        print('YES')
                        return
    print('NO')
    
run()

