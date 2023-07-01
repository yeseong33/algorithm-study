import sys
from collections import deque
n, m = map(int, sys.stdin.readline().split())

board = []

for i in range(n):
    k = list(sys.stdin.readline().strip())
    board.append(k)
    
for i in range(n):
    for j in range(m):
        
        if board[i][j] == 'R':
            R = [i, j]
            board[i][j] = 0
        elif board[i][j] == 'B':
            B = [i, j]
            board[i][j] = 0
        elif board[i][j] == '#':
            board[i][j] = 1
        elif board[i][j] == 'O':
            gool = [i, j]
            board[i][j] = 2
        else:
            board[i][j] = 0
            
# for i in board:
#     print(*i)
# print('b')
# print()
visited = []

def bfs(x, y):
    q = deque()
    lev = 0
    q.append([x, y, 0])
    ans = -1
    l = 0
    while q:
        r, b, l = q.popleft()
        if l == 11:
            break
        
        if r == gool and b != gool:
            # tmp = [item[:] for item in board]
            # tmp[r[0]][r[1]] = 'R'
            # tmp[b[0]][b[1]] = 'B'
            # for jj in tmp:
            #     print(*jj)
            # print()
            # print('pass')
            ans = l
            return ans
        
        # tmp = [item[:] for item in board]
        # tmp[r[0]][r[1]] = 'R'
        # tmp[b[0]][b[1]] = 'B'
        # for jj in tmp:
        #     print(*jj)
        # print()
        
        l += 1
        for i in range(4):
            check ,mr, mb = move(r, b, i)
            if check and [mr, mb] not in visited:
                visited.append([mr, mb])
                q.append([mr, mb, l])
                
            
    return ans


def move(r, b, dir):
    rx, ry = r[0], r[1]
    bx, by = b[0], b[1]
    t = True
    
    # 위
    if dir == 0:
        # 먼저 움직일 공
        if rx < bx:
            while board[rx][ry] != 1:
                rx -= 1
                if board[rx][ry] == 2:
                    rx -= 1
                    break 
            rx += 1
            while board[bx][by] != 1 and [rx, ry] != [bx, by]:
                bx -= 1
                if board[bx][by] == 2:
                    bx -= 1
                    t = False
                    break 
            bx += 1
        else:
            while board[bx][by] != 1:
                bx -= 1
                if board[bx][by] == 2:
                    bx -= 1
                    t = False
                    break 
            bx += 1
            while board[rx][ry] != 1 and [rx, ry] != [bx, by]:
                rx -= 1
                if board[rx][ry] == 2:
                    rx -= 1
                    break 
            rx += 1
            
    # 아래
    elif dir == 1:
        # 먼저 움직일 공
        if rx > bx:
            while board[rx][ry] != 1:
                rx += 1
                if board[rx][ry] == 2:
                    rx += 1
                    break
            rx -= 1
            while board[bx][by] != 1 and [rx, ry] != [bx, by]:
                bx += 1
                if board[bx][by] == 2:
                    bx += 1
                    t = False
                    break
            bx -= 1
        else:
            while board[bx][by] != 1:
                bx += 1
                if board[bx][by] == 2:
                    bx += 1
                    t = False
                    break
            bx -= 1
            while board[rx][ry] != 1 and [rx, ry] != [bx, by]:
                rx += 1
                if board[rx][ry] == 2:
                    rx += 1
                    break
            rx -= 1
                
    # 왼쪽
    elif dir == 2:
        # 먼저 움직일 공
        if ry < by:
            while board[rx][ry] != 1:
                ry -= 1
                if board[rx][ry] == 2:
                    ry -= 1
                    break
            ry += 1
            while board[bx][by] != 1 and [rx, ry] != [bx, by]:
                by -= 1
                if board[bx][by] == 2:
                    by -= 1
                    t = False
                    break
            by += 1
        else:
            while board[bx][by] != 1:
                by -= 1
                if board[bx][by] == 2:
                    by -= 1
                    t = False
                    break
            by += 1
            while board[rx][ry] != 1 and [rx, ry] != [bx, by]:
                ry -= 1
                if board[rx][ry] == 2:
                    ry -= 1
                    break
            ry += 1
    
    # 오른쪽
    elif dir == 3:
        # 먼저 움직일 공
        if ry > by:
            while board[rx][ry] != 1:
                ry += 1
                if board[rx][ry] == 2:
                    ry += 1
                    break
            ry -= 1
            while board[bx][by] != 1 and [rx, ry] != [bx, by]:
                by += 1
                if board[bx][by] == 2:
                    by += 1
                    t = False
                    break
            by -= 1
        else:
            while board[bx][by] != 1:
                by += 1
                if board[bx][by] == 2:
                    by += 1
                    t = False
                    break
            by -= 1
            while board[rx][ry] != 1 and [rx, ry] != [bx, by]:
                ry += 1
                if board[rx][ry] == 2:
                    ry += 1
                    break
            ry -= 1
    return t, [rx, ry], [bx, by]

a = bfs(R, B)
print(a)