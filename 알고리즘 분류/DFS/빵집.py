import sys

n, m = map(int, sys.stdin.readline().split())

# 방문 여부
visited = [[0] * m for _ in range(n)]

# 방문 여부 -> 파이프 라인으로 생각, 할당
for i in range(n):
    k = sys.stdin.readline()
    for j in range(m):
        if k[j] == ".":
            visited[i][j] = 0
        else:
            visited[i][j] = 1

# 움직임 위치, -, /, \
d = [(-1, 1), (0, 1), (1, 1)]
# 끝에 도달할 수 있는 파이프 라인
count =0

# dfs 구현
def dfs(x, y):
    global count
    
    # 끝에 도달할 경우 파이프 라인 개수를 늘림
    if y == m-1:
        count += 1        
        # True를 리턴해 다른 방향은 보지 않고, 다음 라인으로 넘어가게 함
        return True

    # 처음 시작시
    if x == 0 and y == 0:
        
        # 모든 라인에 대해 움직여야 함
        for k in range(x, n):
            # 3방향에 대해 검사
            for j in range(3):
                nx = k + d[j][0]
                ny = y + d[j][1]
                # 움직일 수 있을 경우
                if 0 <= nx <= n-1 and 0 <= ny <= m-1:
                    # 아직 방문하지 않음 - 파이프 라인을 둘 수 있음
                    if visited[nx][ny] == 0:
                        # 방문 처리
                        visited[nx][ny] = 1
                        # 다음 위치에서 검사를 위함
                        # True를 반환 -> 끝까지 연결됨, 더이상 움질일 필요 없음 -> brack
                        if dfs(nx, ny):
                            break

    # 처음이 아닐 경우
    else:
        for j in range(3):
            nx = x + d[j][0]
            ny = y + d[j][1]
            
            if 0 <= nx <= n-1 and 0 <= ny <= m-1:
                if visited[nx][ny] == 0:
                    visited[nx][ny] = 1
                    if dfs(nx, ny):
                        # 끝에 도달값을 전달
                        return True
    # 끝에 도달하지 못할 경우 -> false
    return False

# dfs
dfs(0, 0)
# 출력
print(count)