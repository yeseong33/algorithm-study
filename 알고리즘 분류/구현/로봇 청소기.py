import sys
from collections import deque
sys.setrecursionlimit 



n, m = map(int, sys.stdin.readline().split())

x, y, d = map(int, sys.stdin.readline().split())

area = []

if d == 1:
    d = 3
elif d == 3:
    d = 1

for i in range(n):
    k = list(map(int, sys.stdin.readline().split()))
    area.append(k)

# 방문 한 곳을 1으로 표시
# 청소 안 된 곳을 0로 표시
visited = [item[:] for item in area]

# d = (북, 동, 남, 서)

# 북 -> 동
# 동 -> 남
# 남 -> 서
# 서 -> 북


# 북 서 남 동
dir = [(-1, 0), (0, -1), (1, 0), (0, 1)]

def clean(x, y, d, clean_count):
    
    while True:
        p = False
        if visited[x][y] == 0:
            visited[x][y] = 1
            clean_count += 1
        
        for _ in range(4):
            # 방향 90도 틀기
            d += 1
            d = d%4
            
            # 90도 튼 방향의 다음 위치값
            nx = x + dir[d][0]
            ny = y + dir[d][1]
            
            # 갈수 있는 곳이 있을 경우
            if 0 <= nx < n and 0 <= ny < m:
                if visited[nx][ny] == 0:
                     x = nx 
                     y = ny
                     p = True
                     break
        if not p:
            nx = x + dir[(d+2)%4][0]
            ny = y + dir[(d+2)%4][1]
            
            if 0 <= nx < n and 0 <= ny < m and area[nx][ny] != 1:
                x = nx
                y = ny
            else:
                break
    
    return clean_count
                
            
            
            
print(clean(x, y, d, 0)  )
