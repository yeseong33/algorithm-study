import sys
from collections import deque


n, m = map(int, sys.stdin.readline().split())

board = []


for i in range(n):
    k = list(sys.stdin.readline().strip())
    board.append(k)


# 공의 현재 위치 찾기
b_f = False
r_f = False

for i in range(n):
    for j in range(m):
        if board[i][j] == 'B':
            b = [i, j]
            board[i][j] = '.'
            b_f = True
        if board[i][j] == 'R':
            r = [i, j]
            board[i][j] = '.'
            r_f = True
        if b_f and r_f:
            break
    if b_f and r_f:
        break
visited_prime = [[0] * m for _ in range(n)]



# for i in range(n):
#     for j in range(m):
#         if i == 0 or i == n-1:
#             visited[i][j] = 1
#         else:   
#             if board[i][j] == 'O':
#                 continue
#             if board[i][j] != '.':
#                 visited[i][j] = 1


visited_prime[r[0]][r[1]] =1 


            

board_prime = [item[:] for item in board]


# 상 하 좌 우
d = [(-1, 0), (1, 0), (0, -1), (0, 1)]


# 순서 판단, red - True, blue - False
def first(p, red, blue):
    x1, y1 = red
    x2, y2 = blue
    
    if p == 0:
        if x1 <= x2:
            return True
    elif p == 1:
        if x1 >= x2:
            return True
    elif p == 2:
        if y1 <= y2:
            return True
    elif p == 3:
        if y1 >= y2:
            return True
        
    return False

            
def move(p, x, y, board, visited, cor):

    passed = False
    nx = x
    ny = y
    
    if p == 0:
        while True:
            nx -= 1
            if board[nx][ny] == '.':
                if cor == 0:
                    visited[nx][ny] = 1
                continue
            elif board[nx][ny] == 'O':
                passed = True
                board[x][y] = '.'
                break
            else:
                if cor == 0:
                    visited[nx][ny] = 1
                nx += 1
                board[x][y] = '.'
                if cor == 1:
                    board[nx][ny] = 'B'
                else: 
                    board[nx][ny] = 'R'
                break
    elif p == 1:
        while True:
            nx += 1
            if board[nx][ny] == '.':
                if cor == 0:
                    visited[nx][ny] = 1
                continue
            elif board[nx][ny] == 'O':
                board[x][y] = '.'
                passed = True
                break
            else:
                if cor == 0:
                    visited[nx][ny] = 1
                nx -= 1 
                board[x][y] = '.'
                if cor == 1:
                    board[nx][ny] = 'B'
                else: 
                    board[nx][ny] = 'R'
                break
    elif p == 2:
        while True:
            ny -= 1
            if board[nx][ny] == '.':
                if cor == 0:
                    visited[nx][ny] = 1
                continue
            elif board[nx][ny] == 'O':
                board[x][y] = '.'
                passed = True
                break
            else:
                if cor == 0:
                    visited[nx][ny] = 1
                ny += 1 
                board[x][y] = '.'
                if cor == 1:
                    board[nx][ny] = 'B'
                else: 
                    board[nx][ny] = 'R'
                break
    elif p == 3:
        while True:
            ny += 1
            if board[nx][ny] == '.':
                if cor == 0:
                    visited[nx][ny] = 1
                continue
            elif board[nx][ny] == 'O':
                board[x][y] = '.'
                passed = True
                break
            else:
                if cor == 0:
                    visited[nx][ny] = 1
                ny -= 1
                board[x][y] = '.'
                if cor == 1:
                    board[nx][ny] = 'B'
                else: 
                    board[nx][ny] = 'R'
                break
    
    return nx, ny, passed
        


def BFS(r, b, ans):
    
    start = r+b
    start.append(visited_prime)
    q = deque()
    q.append(start)
    lo = 10
    count = 1
    
    while q:
        if count == 0:
            lo -= 1
            count = len(q)
        
        if lo == 0:
            break
        
        count -= 1
        
        
        r_x, r_y, b_x, b_y, visited = q.popleft()
        
        for i in range(4):
            board = [item[:] for item in board_prime]
            board[r_x][r_y] = 'R'
            board[b_x][b_y] = 'B'
            
            vv = [item[:] for item in visited]
            
            
            nr_x = r_x + d[i][0]
            nr_y = r_y + d[i][1]
            
            red_pass = False
            blue_pass = False
            
            if 0 <= nr_x < n and 0 <= nr_y < m:
                # if board[nr_x][nr_y] == '.':
                if not vv[nr_x][nr_y]:
                    if first(i, (r_x, r_y), (b_x, b_y)):
                        x1, y1, red_pass = move(i, r_x, r_y, board, vv, 0) # 현재 위치 값 반환
                        x2, y2, blue_pass = move(i, b_x, b_y, board, vv, 1) # 현재 위치 값 반환
                    else:
                        x2, y2, blue_pass = move(i, b_x, b_y, board, vv, 1) 
                        x1, y1, red_pass = move(i, r_x, r_y, board, vv, 0)
                    
                    
                    q.append((x1, y1, x2, y2, vv)) ## 현재 위치값 넣어줌
                    
                    
                    # if board[nr_x][nr_y] == 'O':
                    #     ans = True
                    #     print( 'durl')
                    #     print(nr_x, nr_y)
                    #     for tt in board:
                    #         print(*tt)
                    #     return ans                

            if red_pass and not blue_pass:
                ans = True
                # for tt in board:
                #     print(*tt)
                return ans

    return ans
ans = BFS(r, b, False)

if ans:
    print(1)
else:
    print(0)

# 6 7
# #######
# #..B..#
# #R....#
# #....O#
# #.....#
# #######