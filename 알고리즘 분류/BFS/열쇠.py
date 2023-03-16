import sys
from collections import deque


# t = int(input())
t = int(input())

d = [(1, 0), (-1, 0), (0, 1), (0, -1)]

def BFS(visited, key):
    q = deque([(0, 0)])
    sc = 0
    
    while q:
        x, y = q.popleft()
        
        for i in range(4):
            nx = x + d[i][0]
            ny = y + d[i][1]
            
            if 0 <= nx < h + 2 and 0 <= ny < w+2 and visited[nx][ny] != 1:
                if visited[nx][ny] == 0:
                    visited[nx][ny] = 1
                    q.append((nx, ny))
                    
                elif visited[nx][ny] == '$':
                    visited[nx][ny] = 1
                    prime_visited[nx][ny] = 0
                    q.append((nx, ny))
                    sc += 1
                    
                elif visited[nx][ny].islower():
                    key.append(visited[nx][ny])
                    visited[nx][ny] = 1
                    prime_visited[nx][ny] = 0
                    q.append((nx, ny))
                    
                elif not visited[nx][ny].islower():
                    if visited[nx][ny].lower() in key:
                        visited[nx][ny] = 1
                        prime_visited[nx][ny] = 0
                        q.append((nx, ny))

    return sc, key


for _ in range(t):
    h, w = map(int, sys.stdin.readline().split())

    b = [['.'] * (w+2)]
    scrol = 0
    
    for _ in range(h):
        s =  ['.'] + list(sys.stdin.readline().strip()) + ['.']
        b.append(s)
    b.append(['.'] * (w+2))
    
    # key 넣을 리스트
    key = list(sys.stdin.readline().strip())
    if key == ['0']:
        key = []

    
    # 모든 곳을 방문할 수 없을 때까지 돌림 --> 시간초과 나지 않을까?
    save_visited = []
    
    # visited 초기화
    visited = [[0] * (w+2) for _ in range(h+2)]
    for i in range(h+2):
        for j in range(w+2):
            if b[i][j] == ".":
                visited[i][j] = 0
            elif b[i][j] == "*":
                visited[i][j] = 1
            else:
                visited[i][j] = b[i][j]
    prime_visited = [item[:] for item in visited]
    
                
    while True:
        visited  = [item[:] for item in prime_visited]
        save_visited = [item[:] for item in prime_visited]
        
        # BFS 사용
        sc, a_key = BFS(visited, key)

        key = a_key
        scrol += sc

        if prime_visited ==  save_visited: 
            break
        
        
        

        


    print(scrol)
