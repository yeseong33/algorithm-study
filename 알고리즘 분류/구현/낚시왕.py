import sys

row, col, m = map(int, sys.stdin.readline().split())

board = [[[] for i in range(col+1)] for i in range(row+1)]
sharks = []

for i in range(m):
    r, c, s, d, z = map(int, sys.stdin.readline().split())
    board[r][c] = [s, z, d]
    sharks.append([r, c, s, z, d])

def solution(board, row, col, sharks):
    total = 0
    bok = {1: [1,row], 2:row, 3: col, 4:[1,col]}
    bok_d = {1:2, 2:1, 3:4, 4:3}
    
    def make_change(m, p, s, d):
        if m == 2:
            if p == 1:
                if s == 1:
                    return 2, d
                else:
                    if s%2 == 0:
                        return 1, bok_d[d]
                    else:
                        return 2, d
            else:
                if s%2 == 0:
                    return 2, d
                else:
                    return 1, bok_d[d] 
        if m >= p+s:
            np = p + s
            return np, d
        else:
            k = s - (m-p)
            value =  k%(m-1)
            change = 0
            if k%(m-1) == 0:
                change = k//(m-1)
                value = (m-1)
            else: 
                change = k//(m-1)+1
        
        if change%2==0:
            np = 1 + value
            nd = d 
        else:
            np = m - value
            nd = bok_d[d]
            
        
        return np, nd
    def make_chage_2(m, p, s, r_c, d):
        if r_c == 2:
            if p == 1:
                if s%2 == 0:
                    return 1, d
                else:
                    return 2, bok_d[d]
            else:
                if s == 1:
                    return 1, d
                else:
                    if s%2 == 0:
                        return 2, bok_d[d]
                    else:
                        return 1, d
        if m <= p-s:
            np = p-s
            return np, d
        else:
            k = s-(p-m)
            value = k%(r_c-1)
            change = 0
            if k%(r_c-1) == 0:
                change = k//(r_c-1)
                value = (r_c-1)
            else: 
                change = k//(r_c-1)+1 
        if change%2==0:
            nd = d
            np = r_c - value
        else:
            nd = bok_d[d]
            np = 1 + value
        return np, nd
        
    def move(sh):
        x, y, s, size, d = sh
        if d in [2, 3]:
            m = bok[d]
            if d == 2:
                nx, nd = make_change(m, x, s, d)
                ny = y
            elif d == 3:
                ny, nd = make_change(m, y, s, d)
                nx = x
        else:
            m, r_c = bok[d]
            if d == 1:
                nx, nd = make_chage_2(m, x, s, r_c, d)
                ny = y
            else:
                ny, nd = make_chage_2(m, y, s, r_c, d)
                nx = x
        board[nx][ny] = [s, size, nd]
                        
            
    # print(row+1)
    
    # 상어 잡기
    for now in range(1, col+1):
        # print(len(board), 'len')
        # 상어 탐색
        for j in range(1, row+1):
            # print(j, now)
            # print(board[j][now])
            if board[j][now]:
                # 크기만큼 더함
                total += board[j][now][1]
                # 비워주기
                board[j][now] = []    
                break
        sharks.sort(key = lambda x: x[3])
        # 상어 이동
        for shark in sharks:
            if shark[0] == j and shark[1] == now: continue
            if board[shark[0]][shark[1]] == shark[2:]:
                board[shark[0]][shark[1]] = []
            # print(shark)
            
            move(shark)
            # print(board)
        # for t in board[1:]:
        #     print(*t[1:])
        # 상어 리스트 초기화
        sharks.clear()
        for a in range(1, row+1):
            for b in range(1,col+1):
                if board[a][b]:
                    sharks.append([a, b]+board[a][b])
        # print(sharks, 'shehfiwehfie')
        # if now == 3:
        #     return 
    
    print(total)
    return

solution(board, row, col, sharks)

# 3 3 1 
# 2 2 1 4 4
