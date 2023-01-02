import sys

sdo = [list(map(int, sys.stdin.readline().split())) for i in range(9)]
blank = []

for i in range(9):
    for j in range(9):
        if sdo[i][j] == 0:
            blank.append((i, j))

def checkRow(x, a):
    for i in range(9):
        if a == sdo[x][i]:
            return False
    return True

def checkCol(y, a):
    for i in range(9):
        if a == sdo[i][y]:
            return False
    return True 
        
def checkBox(x, y, a):
    nx = x //3*3
    ny = y //3*3
    for i in range(3):
        for j in range(3):
            if a == sdo[nx+i][ny+j]:
                return False
    return True 

def make(d):
    if d == len(blank):
        for i in range(9):
            print(*sdo[i])
        exit(0)
    
    else:
        for i in range(1, 10):
            x = blank[d][0]
            y = blank[d][1]
            
            if checkBox(x, y, i) and checkCol(y, i) and checkRow(x, i):
                sdo[x][y] = i
                make(d+1)
                sdo[x][y] = 0
                



make(0)

## 다시 풀기
