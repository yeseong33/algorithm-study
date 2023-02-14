import sys

n = int(input())

count = 0
ans = 0

board =[[0 for i in range(n)] for i in range(n)]

def checkQueen(board, queen):
    
    x, y = queen
    
    while x > 0:
        x -= 1
    while x <= n-1:
        board[x][y] = 1
        x += 1
        
    x, y = queen
    
    while y > 0:
        y -= 1
    while y <= n-1:
        board[x][y] = 1
        y += 1
    
    x, y = queen
    
    while x < n-1 and y > 0:
        x = x + 1
        y = y - 1
    
    while x >= 0 and  y <= n-1:
        board[x][y] = 1
        x -= 1
        y += 1
        
    x, y = queen
    
    while x > 0 and y > 0:
        x = x - 1
        y = y - 1
    
    while x <= n-1 and y <= n-1:
        board[x][y] = 1
        x += 1
        y += 1
        
    return board

def cleanQueen(board, queen):
    
    x, y = queen
    
    while x > 0:
        x -= 1
    while x <= n-1:
        board[x][y] = 0
        x += 1
        
    x, y = queen
    
    while y > 0:
        y -= 1
    while y <= n-1:
        board[x][y] = 0
        y += 1
    
    x, y = queen
    
    while x < n-1 and y > 0:
        x = x + 1
        y = y - 1
    
    while x >= 0 and  y <= n-1:
        board[x][y] = 0
        x -= 1
        y += 1
        
    x, y = queen
    
    while x > 0 and y > 0:
        x = x - 1
        y = y - 1
    
    while x <= n-1 and y <= n-1:
        board[x][y] = 0
        x += 1
        y += 1
        
    return board

def bfs(test):
    global count, ans
    print(ans)
    if count == 8:
        ans += 1
    
    else:
        for i in range(n):
            for j in range(n):
                if test[i][j] == 0:
                    board_c = [item[:] for item in test]
                    thisBoard = checkQueen(board_c, (i,j))
                    count += 1
                    bfs(thisBoard)
                    thisBoard = cleanQueen(board_c, (i,j))
                    count -= 1

bfs(board)
print(ans)





# [0, 0, 1, 1, 1, 0, 0, 0]
# [1, 1, 1, 1, 1, 1, 1, 1]
# [0, 0, 1, 1, 1, 0, 0, 0]
# [0, 1, 0, 1, 0, 1, 0, 0]
# [1, 0, 0, 1, 0, 0, 1, 0]
# [0, 0, 0, 1, 0, 0, 0, 1]
# [0, 0, 0, 1, 0, 0, 0, 0]
# [0, 0, 0, 1, 0, 0, 0, 0]

# [[0, 0, 0, 0, 0, 0, 0, 0],
#  [0, 0, 0, 1, 0, 0, 0, 0],
#  [0, 0, 0, 0, 0, 0, 0, 0], 
#  [0, 0, 0, 0, 0, 0, 0, 0],
#  [0, 0, 0, 0, 0, 0, 0, 0], 
#  [0, 0, 0, 0, 0, 0, 0, 0], 
#  [0, 0, 0, 0, 0, 0, 0, 0],
#  [0, 0, 0, 0, 0, 0, 0, 0]]

