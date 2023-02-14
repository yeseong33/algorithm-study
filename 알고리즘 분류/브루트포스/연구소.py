import sys

n, m = map(int, sys.stdin.readline().split())

rab = [[0] * (m+1)]

for i in range(n):
    k = [0]+list(map(int, sys.stdin.readline().split()))
    rab.append(k)
    
blank = []

for i in range(1, n+1):
    x = i
    for j in range(1, m+1):
        y = j
        if rab[x][y] == 0:
            blank.append((x, y))

count = len(blank)
check = [0] * count
ans = 0

        
def virus(test):
    D = ((-1, 0), (1, 0), (0, -1), (0, 1))
    stack = []
    visited = [[False for _ in range(m+1)] for _ in range(n+1)]
    for i in range(1, n+1):
        for j in range(1, m+1):
            if test[i][j] == 2:
                stack.append((i, j))
    
    while stack:
        curr = stack.pop()
        if visited[curr[0]][curr[1]]: 
            continue
        
        visited[curr[0]][curr[1]] = True
        test[curr[0]][curr[1]] = 2
        for i in range(4):
            nr = curr[0] + D[i][0]
            nc = curr[1] + D[i][1]
            
            if nr < 1 or nr > n or nc < 1 or nc > m: 
                continue
            if visited[nr][nc]:
                continue
            if test[nr][nc] == 1:
                continue
            stack.append((nr, nc))
    total = 0 
    for i in test[1:]:
        total += i.count(0)
    return total-n
        

def pick3(wall, idx):
    global rab, ans
    
    if len(wall) == 3:
        rab_c = [item[:] for item in rab]

        for i in wall:
            x = i[0]
            y = i[1]
            rab_c[x][y] = 1
        total = virus(rab_c)
        if total > ans:
            ans = total
        
    
    else:
        for i in range(idx, count):
            wall.append(blank[i])
            pick3(wall, i+1)
            wall.pop()



import cProfile

cProfile.run("pick3([], 0)")
print(ans)


# 리스트의 깊은 복사, dfs, 재귀 함수