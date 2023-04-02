import sys
from collections import deque 

n, m = map(int, sys.stdin.readline().split())

# map으로 하고싶으나 내장함수이므로 간단하게 arr로 설정
arr = []

for i in range(n):
    # 입력값이 붙어 들어오므로 strip 사용
    arr.append(list(map(int, sys.stdin.readline().strip())))

# 방향을 확인하기 위한 리스트
d = [(1, 0), (-1, 0), (0, 1), (0, -1)]

# 방문 여부 체크, 3차원을 사용해 벽 파괴 여부를 체크
visited = [[[0] * 2 for _ in range(m)] for _ in range(n)]

# 시작 위치 방문처리
visited[0][0][0] = 1
    

def BFS(x, y, w):
    
    # FIFO을 사용하기 위한 que
    q = deque()
    q.append((x, y, w))
    
    # BFS 구현을 위한 while문, 모든 곳을 탐색할 때 까지 while
    while q:
        
        # que에 들어있는 정보를 FIFO로 꺼냄 
        x, y, w = q.popleft()
        
        # 종료조건, 만약 n, m에 도달하면 멈춤
        if x == n-1 and y == m-1:
            return visited[x][y][w]
        
        # 4방향에 대해서 탐색
        for i in range(4):
            nx = x + d[i][0]
            ny = y + d[i][1]
            
            # 범위 내에 있는지 확인
            if 0 <= nx < n and 0 <= ny < m:
                
                # 벽이고 부술 수 있는 경우
                if arr[nx][ny] == 1 and w == 0:
                    # 현재 값에서 1을 증가시킨 값을 다음 값에 할당 -> 이동 거리 계산
                    visited[nx][ny][1] = visited[x][y][0] + 1
                    q.append((nx, ny, 1))
                    
                # 벽이 아니고 이동할 수 있는 경우
                elif arr[nx][ny] == 0 and visited[nx][ny][w] == 0:
                    visited[nx][ny][w] = visited[x][y][w] + 1
                    q.append((nx, ny, w))
    
    # 종료조건을 만족하지 못할경우
    return -1

print(BFS(0, 0, 0))