import sys
from collections import deque
n, m = map(int, sys.stdin.readline().split())


board = [[0] *(11) for i in range(11)]
for i in range(1, 11):
    for j in range(1, 11):
        board[i][j] = [j + 10 *(i-1), 0, 0]


for i in range(n):
    a, b = map(int, sys.stdin.readline().split())
    a_10 = a//10 + 1
    a_least = a%10
    if a_least == 0:
        a_10 -= 1
        a_least = 10
    x = a_10
    y = a_least
    board[x][y] = [a, 1, b]
    print(x, y, a)

for i in range(m):
    a, b = map(int, sys.stdin.readline().split())
    a_10 = a//10 + 1
    a_least = a%10
    if a_least == 0:
        a_10 -= 1
        a_least = 10
    x = a_10
    y = a_least
    board[x][y] = [a, 1, b]



def bfs(v):
    q = deque()
    visited = [[0] * 11 for i in range(11)]
    lev = 0
    q.append([v, lev])
    ans = 0 
    while q:
        value, lev = q.popleft()
        i = value//10 + 1
        j = value%10
        if j == 0:
            i -= 1
            j = 10
        
        # 자기 위치가 특수할 경우
        if board[i][j][1] == 1:
            visited[i][j] = 1
            value = board[i][j][2]
            
        # 게임이 끝났는지 판단
        if value == 100:
            ans = lev
            break        
        
            
        # 현재 위치에서 다음 주사위 굴리기
        lev += 1
        for k in range(1, 7):
            new_value = value + k
            ni = new_value//10 + 1
            nj = new_value%10
            if nj == 0:
                ni -= 1
                nj = 10
            # print('값: ', new_value, ni, nj)
            # for jj in visited[1:]:
            #     print(*jj[1:])
            if 1 <= ni <= 10 and 1 <= nj <= 10 and not visited[ni][nj]:
                visited[ni][nj] = 1
                q.append([new_value, lev])
        
    return ans

a = bfs(1)
print(a)
