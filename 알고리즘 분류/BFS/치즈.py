import sys
from collections import deque

# 입력값
n, m = map(int, sys.stdin.readline().split())

# 치즈를 담을 공간
chez = []

# 치즈를 넣음
for i in range(n):
    k = list(map(int, sys.stdin.readline().split()))
    chez.append(k)

# 이동 위치 값
d = [(0, 1), (1, 0), (-1, 0), (0, -1)]

# 빈공간을 찾아주는 함수    
def findAir(visited):
    # 빈공간의 위치를 넣을 리스트
    air = []
    for i in range(n):
        # 첫줄과 마지막줄은 모든 위치를 넣음, 방문처리
        if i == 0 or i == n-1:
            for j in range(m):
                air.append((i, j))
                visited[i][j] = 1
        # 나머지 줄은 처음과 끝 위치만 넣음, 방문처리
        else:
            air.append((i, 0))
            air.append((i, m-1))            
            visited[i][0] = 1
            visited[i][m-1] = 1
                
    return air

# 2차원 리스트의 모든 원소가 0인지 확인
def check_zero(chez):
    # 하나라도 값이 존재하면 -> false
    for i in range(n):
        if any(chez[i]):
            return False
    # 모든 값이 0이라면 -> true
    return True


# bfs 이용
def bfs():
    # 방문처리
    visited = [[0] * m for i in range(n)]
    # 큐
    q = deque()
    # 비어있는 공간을 받음
    air = findAir(visited)
    # 현재 단계에서 치즈가 몇개 있는지 확인
    chez_count = 0
    # 공기가 있는 위치값을 초기 q에 할당
    for a in air:
        q.append(a)
    # 모든곳을 방문할 때 까지 
    while q:
        # 가장 왼쪽의 값을 pop
        x, y = q.popleft()
        # 현재 위치에서 4방향에 대해 처리
        for i in range(4):
            nx = x + d[i][0]
            ny = y + d[i][1]
            # 경계선을 넘지 않게 함
            if 0 <= nx <= n-1 and 0 <= ny <= m-1:
                # 방문한적이 없고, 그 공간이 0일 경우에는 q에 넣음
                if visited[nx][ny] == 0 and chez[nx][ny] == 0:
                    q.append((nx, ny))
                # 치즈일 경우에는 공기와 밀접해 있으므로, 0를 할당 및 치즈 개수 증가
                if chez[nx][ny] == 1:
                    chez[nx][ny] = 0
                    chez_count += 1
                # 방문처리
                visited[nx][ny] = 1
    # 처리한 치즈 개수를 반환
    # 모든 치즈가 녹기 전 시간에 있던 치즈의 개수
    return chez_count
                
# 시간을 잼
count_time = 0
# 모든 치즈가 녹을 때까지
while not check_zero(chez):
    # bfs를 수행하며 치즈 개수를 받음
    cc = bfs()
    # 시간 증가
    count_time += 1

# 값 출력
print(count_time)
print(cc)

