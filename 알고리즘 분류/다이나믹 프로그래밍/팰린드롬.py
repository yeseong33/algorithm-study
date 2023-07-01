import sys

n = int(input())

nums = [0]+ list(map(int, sys.stdin.readline().split()))

m = int(input())

board = [[0] * (n+1) for i in range(n+1)]

def isP(leng, start, end):
    # if leng % 2 != 0:
    if board[leng-1][start] == 1:
        if board[leng-2][start] == 1 and nums[start] == nums[end]:
            board[leng][start] = 1
        else:
            board[leng][start] = 0
    else:
        if board[leng-2][start+1] == 1 and nums[start] == nums[end]:
            board[leng][start] = 1
        else:
            board[leng][start] = 0
    # else:
    #     if board[leng-1][start] == 1:
    #         if board[leng-2][start] == 1:
    #             board[leng][start] = 1
    #         else:
    #             board[leng][start] = 0
    #     else:
    #         if board[leng-2][start+1] == 1 and nums[start] == nums[end]:
    #             board[leng][start] = 1
    #         else:
    #             board[leng][start] = 0

# 3
# 1 11 111
# 1
# 1 3
# 3
# 1 1 1
# 1
# 1 2

# i = len(), j = start, end = diff - j 
for i in range(1, n+1):
    for j in range(1, n+1-i +1):
        if i == 1:
            board[i][j] = 1
        elif i == 2:
            if nums[i+j-1] == nums[j]:
                board[i][j] = 1
        else:
            isP(i, j, i+j-1)
        
        
                


for i in range(m):
    s, e = map(int, sys.stdin.readline().split())
    di = e-s+1
    print(board[di][s])