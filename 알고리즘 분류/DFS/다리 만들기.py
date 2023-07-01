import sys

n, m = map(int, sys.stdin.readline().split())

board = []

for i in range(n):
    k = list(map(int, sys.stdin.readline().split()))
    board.append(k)
    


visited = [[0] *m for i in range(n)]
d = [(1, 0), (-1, 0), (0, 1), (0, -1)]
po = 2
def dfs(x, y, p):
    visited[x][y] = 1
    
 
    if board[x][y] == 1:
        board[x][y] = p
        for k in range(4):
            nx = x + d[k][0]
            ny = y + d[k][1]
            if 0 <= nx < n and 0 <= ny < m:
                if not visited[nx][ny]:
                    dfs(nx, ny, p)
        return True
    return False

        
                    
for i in range(n):
    for j in range(m):
        if dfs(i, j, po):
            po += 1

# for jj in board:
#     print(*jj)
# print()

bridge = []
                
def make_da(x, y, land, dir, c):

    if board[x][y] != 0 and board[x][y] != land:
        # print(x, y)
        if c > 1:
            bridge.append([land, board[x][y], c])
        return

    if board[x][y] == 0:
        nx = x + d[dir][0] 
        ny = y + d[dir][1]
        if 0 <= nx < n and 0 <= ny < m:
             make_da(nx, ny, land, dir, c+1)


visited_b = [[0] *m for i in range(n)]
for i in range(n):
    for j in range(m):
        if board[i][j] != 0:
            for k in range(4):
                ni = i + d[k][0] 
                nj = j + d[k][1]  
                if 0 <= ni < n and 0 <= nj < m:
                    make_da(ni, nj, board[i][j], k, 0)
# print(bridge)

bridge.sort(key = lambda x: x[2])

v = po-2
parent = [i for i in range(v+1)]
cost = 0

def find_parent(parent, x):
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])
    return parent[x]

def union_parent(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)

    if a < b:
        parent[b] = a
    else:
        parent[a] = b
count = 0
for k in bridge:
    a, b, c = k
    a = a-1
    b = b-1
    if find_parent(parent, a) != find_parent(parent, b):
        union_parent(parent, a, b)
        cost += c
        count +=1 

if cost == 0 or count != v-1:
    print(-1)
else:
    print(cost)
    
# 9 6
# 0 0 0 0 1 0 
# 0 0 0 0 0 0 
# 0 1 0 0 0 1 
# 0 0 0 0 0 0 
# 0 0 0 0 0 0 
# 0 1 0 0 1 1 
# 0 0 0 0 0 0 
# 0 0 0 0 0 0 
# 0 1 0 0 0 01