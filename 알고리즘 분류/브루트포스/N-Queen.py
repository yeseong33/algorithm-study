import sys

n = int(input())

count = 0
ans = 0

board =[[0 for i in range(n)] for i in range(n)]

def checkQueen(board, queen):
    
    x, y = queen
    board_c = [item[:] for item in board]
    
    

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

