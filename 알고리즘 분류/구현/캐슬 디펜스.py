import sys

n, m, d = map(int, sys.stdin.readline().split())

board = []

for i in range(n):
    k = list(map(int, sys.stdin.readline().split()))
    board.append(k)

def aRange(a):
    x = a[0]
    y = a[1]
    a_atack = []
    for i in range(-1, -(d+1), -1):
        for j in range(-d+1, d-1+1):
            if 0 <= x+i < n and 0 <= y+j < m:
                value = abs(i) + abs(j)
                if value <= d:
                    a_atack.append([x+i, y+j])
    return a_atack
    
def play(a, b, c):
    global board
    
    a_Range = []
    count = 0

    tmp_board = [item[:] for item in board]
    
    for i in [a, b, c]:
        k = aRange(i)
        k.sort(key=lambda x: (abs(i[0]-x[0]) + abs(i[1]-x[1]), x[1]) )
        a_Range.append(k)
    t = True
    
    
    while t:

        for arc in a_Range:
            for a in arc:
                if tmp_board[a[0]][a[1]] == 1:
                    tmp_board[a[0]][a[1]] = 2
                    count += 1
                    break
                elif tmp_board[a[0]][a[1]] == 2:
                    break
        
        t = False
        
        for i in range(n):
            for j in range(m):
                if tmp_board[i][j] == 2:
                    tmp_board[i][j] = 0
                elif tmp_board[i][j] == 1:
                    t = True
        
        
        tmp_board = [[0] * m] + tmp_board
        tmp_board.pop()
        
        
    return count

visited = [0] * m
ac = []
mac = 0
def dfs(idx):
    global mac
    if len(ac) == 3:
        hhh = [[n, ac[0]], [n, ac[1]], [n, ac[2]]]
        ccc = play(hhh[0], hhh[1], hhh[2])
        if ccc > mac:
            mac = ccc
        return
    
    for i in range(idx, m):
        if not visited[i]:
            ac.append(i)
            visited[i] = 1 
            dfs(i)
            visited[i] = 0
            ac.pop()
            
dfs(0)

print(mac)

# 7 6 2
# 0 1 1 0 1 0
# 1 1 0 1 0 0
# 1 0 1 0 0 1
# 0 1 0 0 1 0
# 1 0 0 1 0 1
# 0 0 1 0 1 1
# 0 1 0 1 1 0