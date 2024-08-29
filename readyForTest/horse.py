import sys

def makeSettings():
    n, k = map(int, sys.stdin.readline().split())
    board = []
    hc = 0
    for _ in range(n):
        tmp = list(map(int, sys.stdin.readline().split()))
        board.append(tmp)
    playBoard = [[[] for i in range(n)] for i in range(n)]

    for o in range(1, k+1):
        x, y, d = map(int, sys.stdin.readline().split())
        if playBoard[x-1][y-1] == []:
            hc += 1
        playBoard[x-1][y-1].append([o, d])
    
    dir = [(0, 0), (0, 1), (0, -1), (-1, 0), (1, 0)]

    return board, playBoard, n, k, dir


def play(num, n, dir, board, playBoard):
    # 판에서 해당 번호가 - 가장 아래에 있을 때 움직을 수 있음
    for x in range(n):
        for y in range(n):
            if playBoard[x][y] != []:
                if isBottom(x, y, num, playBoard):
                    move(x, y, n, dir, board, playBoard, False)
                    return

def isBottom(x, y, num, playBoard):
    if playBoard[x][y][0][0] == num:
        return True
    return False

def move(x, y, n, dir, board, playBoard, blue):
    d = playBoard[x][y][0][1]
    # 한칸 움직임
    nx = x + dir[d][0]
    ny = y + dir[d][1]

    # 조건에 따라
    if 0 <= nx < n and 0<= ny < n:
        color = whatColor(nx, ny, board)
        if color == 'W':
            now = playBoard[x][y].copy()
            playBoard[nx][ny] = playBoard[nx][ny] + now
            playBoard[x][y] = []
        elif color == 'R':
            now = playBoard[x][y].copy()
            playBoard[nx][ny] = playBoard[nx][ny] + now[-1::-1]
            playBoard[x][y] = []
        else:
            if blue:
                return 
            now = playBoard[x][y][0] 
            if now[1]%2==1:
                playBoard[x][y][0][1] += 1
            else:
                playBoard[x][y][0][1] -= 1
            move(x, y, n, dir, board, playBoard, True)
    else:
        if blue:
            return 
        now = playBoard[x][y][0] 
        if now[1]%2==1:
            playBoard[x][y][0][1] += 1
        else:
            playBoard[x][y][0][1] -= 1
        move(x, y, n, dir, board, playBoard, True)


def whatColor(x, y, board):
    if board[x][y] == 0:
        return 'W'
    elif board[x][y] == 1:
        return 'R'
    else:
        return 'B'

def isEnd(n, playBoard):
    for x in range(n):
        for y in range(n):
            if playBoard[x][y] != []:
                if len(playBoard[x][y]) >= 4:
                    return True
    return False

def solve():
    board, playBoard, n, k,  dir = makeSettings()

    for round in range(1, 1001):
            # 한판이 돌아감 - 순서대로 한번씩
        for num in range(1, k+1):
            play(num, n, dir, board, playBoard)
            if isEnd(n, playBoard):
                print(round)
                return
    print(-1)
solve()




