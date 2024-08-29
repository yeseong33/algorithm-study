import sys
import heapq


def makeSettings():
    n, m = map(int, sys.stdin.readline().split())
    board = [list(sys.stdin.readline().strip()) for i in range(n)]
    b = []
    r = []
    visited = [[[[0] * 10 for i in range(10)] for _ in range(10)] for i in range(10)]
    for i in range(n):
        for j in range(m):
            NOW = board[i][j]
            if NOW == "B":
                b = [i, j]
                board[i][j]="."
            elif NOW == "R":
                r = [i, j]
                board[i][j]="."
                
    dir = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    visited[r[0]][r[1]][b[0]][b[1]] = 1

    return b, r, dir, board, visited

def move(condition, x, y, ox, oy, board):
    PASS_ = True
    if not condition:
        nbx = x + dir[d][0]
        nby = y + dir[d][1]
        if board[nbx][nby] == "O":
            condition = True
            x, y = -2, -2
        elif board[nbx][nby] =="#" or [nbx, nby]==[ox, oy]:
            PASS_ = False
        else:
            x, y = nbx, nby
    else:
        PASS_ = False

    return PASS_, x, y 

def BFS(red, blue, board, dir, visited):
    q = [(1, red, blue)]
    while q:
        count, red, blue = heapq.heappop(q)
        orx, ory = red[0], red[1]
        obx, oby = blue[0], blue[1]
        
        # 방향이 정해지고
        for d in range(4):
            gameOver = False
            gameFinish = False
            PASS_BLUE = True
            PASS_RED = True
            rx, ry, bx, by = orx, ory, obx, oby
            # 움직임이 끝날때까지 둘다 못움직일때 움직임
            while PASS_BLUE or PASS_RED:
                PASS_BLUE = True
                PASS_RED = True


                move(gameOver, bx, by, rx, ry, board)

                if not gameFinish: 
                    nrx = rx + dir[d][0]
                    nry = ry + dir[d][1]
                    if board[nrx][nry] == "O":
                        gameFinish = True
                        rx, ry = -1, -1
                    elif board[nrx][nry] == "#" or [nrx, nry]==[bx, by]:
                        PASS_RED = False
                    else:
                        rx, ry = nrx, nry
                else :
                    PASS_RED = False

                
            if gameFinish and not gameOver:
                return count
            elif not gameOver and count < 10 and visited[rx][ry][bx][by] == 0:
                visited[rx][ry][bx][by] = 1
                heapq.heappush(q, (count+1,[rx, ry], [bx, by]))
                    



def solve():
    b, r, dir, board, visited = makeSettings()
    count = BFS(r, b, board, dir, visited)
    if count == None:
        print(-1)
    else:
        print(count)

solve()

