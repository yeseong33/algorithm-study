import sys


n = int(input())

board = [[0] * 101 for i in range(101)]

dir = [(0, 1), (-1, 0), (0, -1), (1, 0)]


def check(b, a, y, x):
    if a == x and b == y:
        return b, a
    
    if (a-x)< 0 and b-y < 0:
        a, b = x+abs(b-y), y-abs(a-x)
    elif a-x > 0 and b-y > 0:
        a, b = x-abs(b-y), y + abs(a-x)    
    elif a-x < 0 and b-y > 0:
        a, b = x-abs(b-y), y-abs(a-x)
    elif a-x > 0 and b-y < 0:
        a, b = x+abs(b-y), y+abs(a-x)
    elif b == y:
        if a - x > 0:
            a, b = x, y + abs(a-x)
        else:
            a, b = x, y -abs(a-x)
    else:
        if b-y > 0:
            a, b = x - abs(b-y), y
        else:
            a, b = x+abs(b-y), y
    return b, a


def makeDragon(x, y, d, g):
    
    main = (y + dir[d][0], x + dir[d][1])
    
    dragon = [(y, x), main]
    
    board[main[0]][main[1]] = 1
    board[y][x] = 1
    
    for _ in range(g):
        
        dl  = len(dragon)
        
        for i in range(dl-2, -1, -1):
            now = dragon[i]
            y_t = now[0]
            x_t = now[1]
            y_t, x_t = check(y_t, x_t, main[0], main[1])
            board[y_t][x_t] = 1
            dragon.append((y_t, x_t))
        
        main = dragon[-1]
            

for i in range(n): 
    x, y, d, g = map(int, sys.stdin.readline().split())
    makeDragon(x, y, d, g)

count = 0 
cdir = [(0, 1), (1, 0), (1, 1)]
for i in range(100):
    for j in range(100):
        if board[i][j] == 1:
            t = 0
            for k in range(3):
                if board[i+cdir[k][0]][j+cdir[k][1]] == 1: 
                    t += 1
            if t == 3:
                count += 1

print(count)



