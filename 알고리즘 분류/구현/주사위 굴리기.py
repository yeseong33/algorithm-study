import sys

n, m, x, y, k = map(int, sys.stdin.readline().split())


Map = []

for i in range(n):
    k = list(map(int, sys.stdin.readline().split()))
    Map.append(k)

orders = list(map(int, sys.stdin.readline().split()))

# 주사위
dice = [[[0 for _ in range(3)] for _ in range(3)] for _ in range(3)]




def roll(order):
    # 동
    if order == 1:
        dice[0][1][1], dice[1][1][2], dice[2][1][1], dice[1][1][0]  = \
            dice[1][1][0], dice[0][1][1], dice[1][1][2], dice[2][1][1]  
    
    # 서
    elif order == 2:
        dice[1][1][0], dice[0][1][1], dice[1][1][2], dice[2][1][1] =\
            dice[0][1][1], dice[1][1][2], dice[2][1][1], dice[1][1][0]
    
    # 북
    elif order == 3:
        dice[1][0][1], dice[0][1][1], dice[1][2][1], dice[2][1][1] =\
            dice[0][1][1], dice[1][2][1], dice[2][1][1], dice[1][0][1]
            
    # 남
    elif order == 4:
        dice[0][1][1], dice[1][2][1], dice[2][1][1], dice[1][0][1] =\
            dice[1][0][1], dice[0][1][1], dice[1][2][1], dice[2][1][1]
            
        
        

d = [(0, 1), (0, -1), (-1, 0), (1, 0)]


for order in orders:
    
    # 굴리기
    nx = x + d[order-1][0]
    ny = y + d[order-1][1]
    
    # print(x, y, 'old')
    # print(nx, ny, 'new')
    
    # 막히면 -> 스킵
    if not (0 <= nx < n and 0 <= ny < m):
        # print('ok')
        continue
    
    
    roll(order)
    
    if Map[nx][ny] == 0:
        Map[nx][ny] = dice[2][1][1]
    else:
        dice[2][1][1] = Map[nx][ny]
        Map[nx][ny] = 0
    
    print(dice[0][1][1])
    
    # for i in dice:
    #     print(*i, 'all')
    
    x, y = nx, ny
    