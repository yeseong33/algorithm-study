import sys
from collections import deque

n = int(input())

space = []

for i in range(n):
    k = list(map(int, sys.stdin.readline().split()))
    space.append(k)
    


# 물고기 까지의 최단 거리
d = [(1, 0), (-1, 0), (0, 1), (0, -1)]

def bfs(x, y, size):
    q = deque()
    q.append((x, y))
    count = 1
    
    visited[x][y] = 1
    ans = []
    time = 0
    key = (-1, -1)
    
    while q:
        if count == 0:
            time +=1
            # 가장 짧은 거리 찾음
            for i in q:
                x1, y1 = i
                if space[x1][y1] and space[x1][y1] < size:
                    ans.append((x1, y1))
            if ans:
                ans.sort()
                key = ans[0]
                break
            count = len(q)
        x, y = q.popleft()
        count -= 1
        
        for i in range(4):
            nx = x +d[i][0]
            ny = y +d[i][1]
            
            if 0 <= nx < n and 0 <= ny < n:
                if not visited[nx][ny] and space[nx][ny] <= size:
                    q.append((nx, ny))
                    visited[nx][ny] = 1
    return key, time

# 아기상어 위치 찾기
b = False
for i in range(n):
    for j in range(n):
        if space[i][j] == 9:
            x = i
            y = j
            b = True
            break
    if b:
        break

# 물고기를 먹는 과정
size = 2
grow = 0 
total_time = 0
while True:
    
    # 현제 상어 위치에서 가장 짧은 거리 반환
    visited = [[0] * n for _ in range(n)]
    key, time = bfs(x, y, size)
    
    nx = key[0] 
    ny = key[1] 

    # 갈 수 있는 곳이 없을 경우 
    if nx == -1:
        break
    
    # 물고기를 먹었을 경우
    grow += 1
    if grow == size:
        size += 1
        grow = 0
    total_time += time
    
    # 상어 현재 위치 보정
    space[x][y] = 0
    space[nx][ny] = 9

    x = nx
    y = ny
     
print(total_time)

