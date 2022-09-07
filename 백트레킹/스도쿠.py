import sys

sdo = [list(map(int, sys.stdin.readline().split())) for i in range(9)]

num = [1, 2, 3, 4, 5, 6, 7, 8, 9]
c = 0 


def make(d):
    global c
    if d == 9:
        if c == 1:
            return 
        for i in range(9):
            k = 0
            for j in range(9):
                k += sdo[j][i]
            if k != 45:
                return

        t = 0 
        for i in range(0, 9, 3):
            for j in range(0, 9, 3):
                t = sdo[i][j] + sdo[i][j+1] + sdo[i][j+2] +\
                    sdo[i+1][j] + sdo[i+1][j+1] + sdo[i+1][j+2] +\
                    sdo[i+2][j] + sdo[i+2][j+1] + sdo[i+2][j+2]
                if t != 45: 
                    return
                
        for i in sdo:
            print(' '.join(map(str, i)))
        exit(0)
        return             
    
    else:
        
        for i in range(1, 10):
            if i not in sdo[d]:
                idx = sdo[d].index(0)
                sdo[d][idx] = i
                if sdo[d].count(0) != 0:
                    make(d)
                else:
                    make(d+1)
                sdo[d][idx] = 0

make(0)
                
                    

