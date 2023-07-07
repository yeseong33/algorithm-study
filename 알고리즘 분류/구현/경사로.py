import sys

n, l = map(int, sys.stdin.readline().split())

board = []

for i in range(n):
    k = list(map(int, sys.stdin.readline().split()))
    board.append(k)


ans = []

def ho():
    # 가로 방향 체크
    i = 0
    j = 0
    p = True
    visited = [[0] * n for i in range(n)]
    while i < n:
        while True:
            now = board[i][j]
            ni = i
            nj = j + 1
            # 길 성공
            if nj == n:
                ans.append(i)
                break
            next = board[ni][nj]
            # 오르막길일 경우
            if next - now == 1:
                bi = i
                bj = j - l + 1
                if bj >= 0 and not visited[bi][bj]:
                    tmp = board[bi][bj]
                    visited[bi][bj] = 1
                    for k in range(l-1):
                        if visited[bi][bj+1]:
                            p = False
                            break
                        next_tmp = board[bi][bj+1]
                        visited[bi][bj+1] = 1
                        if tmp != next_tmp:
                            # 안돼
                            p = False
                            break
                        bj += 1
                    
                else:
                    # 안돼
                    p = False
                    break
                # 길 완성
                i = ni
                j = nj
            # 내리막길
            elif now - next == 1:
                ai = i
                aj = j + l
                if aj < n and not visited[ai][aj]:
                    aj = j + 1
                    tmp = board[ai][aj]
                    visited[ai][aj] = 1
                    for k in range(l-1):
                        if visited[ai][aj+1]:
                            p = False
                            break
                        next_tmp = board[ai][aj+1]
                        visited[ai][aj+1] = 1
                        if tmp != next_tmp:
                            # 안돼
                            p = False
                            break
                        aj += 1
                else:
                    # 안돼
                    p = False
                    break
                # 길 완성
                i = ni
                j = nj
            # 높이가 같을 경우
            elif now == next:
                i = ni
                j = nj
            
            else:
                # 안돼
                p = False
                break
            
            if not p:
                break
        
        i += 1
        j = 0
        p = True

def ve():
    # 세로 방향 체크
    i = 0
    j = 0
    p = True
    visited = [[0] * n for i in range(n)]
    while j < n:
        while True:
            now = board[i][j]
            ni = i + 1
            nj = j
            # 길 성공
            if ni == n:
                ans.append(j)
                break
            next = board[ni][nj]
            # 오르막길일 경우
            if next - now == 1:
                bi = i - l + 1
                bj = j 
                if bi >= 0 and not visited[bi][bj]:
                    tmp = board[bi][bj]
                    visited[bi][bj] = 1
                    for k in range(l-1):
                        if visited[bi+1][bj]:
                            p = False
                            break
                        next_tmp = board[bi+1][bj]
                        visited[bi+1][bj] = 1
                        if tmp != next_tmp:
                            # 안돼
                            p = False
                            break
                        bi += 1 
                else:
                    # 안돼
                    p = False
                    break
                # 길 완성
                i = ni
                j = nj
            # 내리막길
            elif now - next == 1:
                ai = i + l 
                aj = j
                if ai < n and not visited[ai][aj]:
                    ai = i + 1
                    tmp = board[ai][aj]
                    visited[ai][aj] = 1  
                    for k in range(l-1):
                        if visited[ai+1][aj]:
                            p = False
                            break
                        next_tmp = board[ai+1][aj]
                        visited[ai+1][aj] = 1
                        if tmp != next_tmp:
                            # 안돼
                            p = False
                            break
                        ai += 1
                else:
                    # 안돼
                    p = False
                    break
                # 길 완성
                i = ni
                j = nj
            # 높이가 같을 경우
            elif now == next:
                i = ni
                j = nj
            
            else:
                # 안돼
                p = False
                break
            
            if not p:
                break
        
        i = 0
        j += 1
        p = True

ho()
ve()
print(len(ans))