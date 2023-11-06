# -*- coding: utf-8 -*-
import sys

n, m = map(int, sys.stdin.readline().split())

board = []
board_uni = []
for i in range(n):
    tmp = list(sys.stdin.readline().strip())
    board_uni += tmp
    board.append(tmp)

count = 1
stop = False
board_count = [[0] * m for i in range(n)]

for i in range(n):
    if stop:
        break
    for j in range(m):
        if (n-i) * (m-j) < count:
            stop = True
            break
        now = board[i][j]
        
        r_count = 0
        for r in range(j+1, m):
            if board[i][r] != now:
                break
            r_count += 1
            
        d_count = 0
        for d in range(i+1, n):
            if board[d][j] != now:
                break
            d_count += 1
        
        result = d_count * r_count
            
        if result == 0:
            if d_count:
                result = d_count + 1
            elif r_count:
                result = r_count + 1
            
            if result > count:
                count = result
            continue
        
        if (d_count+1) * (r_count+1) <= count: 
            continue
        
        tmp = 0
        find = False
        board_count = [[0] * (r_count+2) for _ in range(d_count+2)]
        for ii in range(i, i+d_count+1):
            if ii >= n:
                break
            for jj in range(j, j+r_count+1):
                if jj >= m:
                    break
                if board[ii][jj] != now:
                    continue
                
                board_count[ii-i+1][jj-j+1] = board_count[ii-i-1+1][jj-j+1] + board_count[ii-i+1][jj-j-1+1] - board_count[ii-i][jj-j] + 1
                if count < board_count[ii-i+1][jj-j+1]:
                    count = board_count[ii-i+1][jj-j+1]       
                
print(count)