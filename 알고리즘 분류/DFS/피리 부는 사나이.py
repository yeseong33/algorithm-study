import sys

n, m = map(int, sys.stdin.readline().split())

maz = []

for i in range(n):
    k = list(sys.stdin.readline().strip())
    maz.append(k)
    
for i in maz:
    print(*i)
visited = [[0] * (m) for i in range(n)]
d = [(-1, 0), (1, 0), (0, -1), (0, 1)]
count = 0
po = 1

def move(i, j):
    
    if maz[i][j] == 'U':
        return i-1, j
    elif maz[i][j] == 'D':
        return i+1, j
    elif maz[i][j] == 'L':
        return i, j-1
    elif maz[i][j] == 'R':
        return i, j+1    
    return

def dfs(x, y, p):
    global count, po
    if visited[x][y]:
        if visited[x][y] == p:
            count += 1
            po += 1
        elif visited[x][y] != p:
            po += 1
        return

    if not visited[x][y]:
        visited[x][y] = p
        ni, nj = move(x, y)
        dfs(ni, nj, p)
            
for i in range(n):
    for j in range(m):
        dfs(i, j, po)
print(count)