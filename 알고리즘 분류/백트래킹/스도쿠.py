import sys
sys.setrecursionlimit(10 ** 8)

sdo = [list(map(int, sys.stdin.readline().split())) for i in range(9)]
zero =[]
zeroCount = 0
count = 0
for i in range(9):
    for j in range(9):
        if sdo[i][j] == 0:
            zeroCount += 1
            zero.append((i,j))
            
zero.sort(reverse=True)

def box(row, col):
    a = row // 3 
    b = col // 3 
    
    count = 0 
    for i in range(3*a, 3*(a+1)):
        for j in range(3*b, 3 * (b+1)):
            if sdo[i][j] == sdo[row][col]:
                count += 1
                
    if count > 1:
        return False
    return True
    
    
    # (00), (01) (02)
    # (10), (11) (12)
    # (20), (21) (22)


def is_promising(x, y):
    count = -2
    
    for j in range(9):
        if sdo[x][j] == sdo[x][y]:
            count += 1
        if sdo[j][y] == sdo[x][y]:
            count += 1
            if x == 0 and y == 3:
                print(sdo[x][j] == sdo[x][y])
                print( sdo[j][y] == sdo[x][y])
                print(box(x, y))
                
    if box(x, y):
        if count == 0:
            return True 
    
    return False
            


def dfs(idx):
    global count, zero
    print(count)
    if  70 < len(zero) + count < 82:
        print(zero)
    
    
    print(str(len(zero)) + '+' + str(count) +'=' + str(len(zero) + count))
    if zeroCount == count:
        for i in sdo:
            print(*i)
        # exit(0)
            
    else:
        i = zero[idx] 
       
        row = i[0]
        col = i[1]
        if is_promising(row, col):
            for j in range(1, 10):
                sdo[row][col] = j
                count += 1
                dfs(idx+1)
                count -= 1
                sdo[row][col] = 0

print(zeroCount)
print(len(zero))
print(count)
print(zero)
dfs(0)

                
                     
# [[1, 3, 5, 4, 6, 9, 2, 7, 8], 
#  [7, 8, 2, 1, 3, 5, 6, 4, 9],
#  [4, 6, 0, 2, 7, 8, 1, 3, 5],
#  [3, 2, 1, 5, 4, 6, 8, 9, 7], 
#  [8, 0, 4, 9, 1, 3, 5, 2, 6],
#  [5, 9, 6, 8, 2, 0, 4, 1, 3], 
#  [9, 1, 7, 6, 5, 2, 1, 8, 3], 
#  [6, 0, 3, 7, 0, 1, 9, 5, 2], 
#  [2, 5, 8, 3, 9, 4, 7, 6, 0]]

# [[1, 3, 5, 4, 6, 9, 2, 7, 8],
#  [7, 8, 2, 1, 3, 5, 6, 4, 9], 
#  [4, 6, 9, 2, 7, 8, 1, 3, 5], 
#  [3, 2, 1, 5, 4, 6, 8, 9, 7], 
#  [8, 7, 4, 9, 1, 3, 5, 2, 6],
#  [5, 9, 6, 8, 2, 7, 4, 1, 3],
#  [9, 1, 7, 6, 5, 2, 1, 8, 3], 
#  [6, 4, 3, 7, 8, 1, 9, 5, 2],
#  [2, 5, 8, 3, 9, 4, 7, 6, 4]]

# 0 0 0 0 0 0 0 0 0
# 0 0 0 0 0 0 0 0 0
# 0 0 0 0 0 0 0 0 0
# 0 0 0 0 0 0 0 0 0
# 0 0 0 0 0 0 0 0 0
# 0 0 0 0 0 0 0 0 0
# 0 0 0 0 0 0 0 0 0
# 0 0 0 0 0 0 0 0 0
# 0 0 0 0 0 0 0 0 0
# [[1, 2, 3, 4, 5, 6, 7, 8, 9], 
#  [4, 5, 6, 1, 2, 3, 0, 0, 0],
#  [9, 7, 8, 0, 0, 0, 3, 1, 2], 
#  [2, 1, 4, 3, 6, 5, 8, 7, 0], 
#  [5, 3, 7, 2, 1, 4, 6, 9, 0], 
#  [8, 6, 9, 7, 0, 0, 1, 2, 3], 
#  [3, 4, 1, 5, 7, 2, 9, 6, 8], 
#  [6, 8, 2, 9, 3, 1, 4, 5, 7],
#  [7, 9, 5, 6, 4, 8, 2, 3, 0]]


    
