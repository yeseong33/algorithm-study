
import sys
from collections import deque 

n = int(input())

road = [[0] * (n+1) for i in range(n+1)]

k = int(input())

for i in range(k):
    x, y = map(int, sys.stdin.readline().split())
    road[x][y] = 1
    
road[1][1] = 3

time = [0] * (n**2 +1)
# print(time)

l = int(input())

for i in range(l):
    x, c = sys.stdin.readline().split()
    a = int(x)
    if c == "D":
        time[a] = 12
    else:
        time[a] = 98

t = 0
x = 1
y = 1

D = ((0, 1), (1, 0), (0, -1), (-1, 0))
dir = (0, 1)

snake = deque([[1, 1]])

while True:
    t += 1
    nx = x + dir[0]
    ny = y + dir[1]
    # print(nx, ny)
    
    # 방향 전환 해두기
    if time[t] == 12:
        idx = (D.index(dir) + 1) % 4
        dir = D[idx]
    elif time[t] == 98:
        idx = (D.index(dir) - 1) 
        dir = D[idx]
    
    # print(nx, ny, 'aft')
    
    ## 죽는 조건
    if nx <= 0 or nx > n or ny <= 0 or ny > n or road[nx][ny] == 3:
        
        break
    
    
    if road[nx][ny] == 1:
        snake.append([nx, ny])
        road[nx][ny] = 3
        
            
    elif road[nx][ny] == 0:
        dx, dy= snake.popleft()

        snake.append([nx, ny])
        # print(nx, ny, 'd')
        road[dx][dy] = 0 
        road[nx][ny] = 3
    
    x, y = nx, ny
    
    # print(snake)
    # for i in road:
    #     print(i)
    # print()
print(t)   
    
#  0 0 0 0 0 0
#  0 0 0 0 1 0
#  0 0 0 1 0 0
#  0 0 0 0 0 0
#  0 0 1 x 0 0
#  0 0 0 x 0 0


# 3
# 8
# 1 2
# 1 3
# 2 3 
# 2 2
# 2 1
# 3 1
# 3 2
# 3 3
# 4
# 2 D
# 3 D
# 5 L
# 6 L