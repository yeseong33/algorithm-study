# import sys


# n = int(input())

# borad = []

# for i in range(n):
#     k = list(map(int, sys.stdin.readline().split()))
#     borad.append(k)
    

# dir = [(1, 0), (1, -1), (1, 1)]

# def dp(x, y):
    
#     if x == n-1:
#         visited[x][y][0] = borad[x][y]
#         visited[x][y][1] = borad[x][y]
#         return
    
    
#     for i in range(3):
#         nx = x + dir[i][0]
#         ny = y + dir[i][1]
        
#         if 0 <= nx < n and 0 <= ny < n:
#             dp(nx, ny)
#             visited[x][y][0] = max(visited[x][y][0], borad[x][y] + visited[nx][ny][0])
            
#             if visited[x][y][1] == -1:
#                 visited[x][y][1] = borad[x][y] + visited[nx][ny][1]
#             else:
#                 visited[x][y][1] = min(visited[x][y][1], borad[x][y] + visited[nx][ny][1])  

# max_score = 0
# min_score = 900001

# for i in range(n):
#     visited = [[[-1, -1]] * n for i in range(n)]

#     dp(0, i)
    
#     if visited[0][i][0] > max_score:
#         max_score = visited[0][i][0]
#     if visited[0][i][1] < min_score:
#         min_score = visited[0][i][1]
        
# print(max_score, min_score)
    
    

import sys


n = int(input())

max_dp = [0] * 3
min_dp = [0] * 3

max_tmp = [0] * 3
min_tmp = [0] * 3

for i in range(n):
    a, b, c= map(int, sys.stdin.readline().split())
    for j in range(3):
        if j == 0:
            max_tmp[j] = a + max(max_dp[j], max_dp[j+1])
            min_tmp[j] = a + min(min_dp[j], min_dp[j+1])
        elif j == 1:
            max_tmp[j] = b + max(max_dp[j-1], max_dp[j], max_dp[j+1])
            min_tmp[j] = b + min(min_dp[j-1], min_dp[j], min_dp[j+1])
        elif j == 2:
            max_tmp[j] = c + max(max_dp[j], max_dp[j-1])
            min_tmp[j] = c + min(min_dp[j], min_dp[j-1])
    
    for j in range(3):
        max_dp[j] = max_tmp[j]
        min_dp[j] = min_tmp[j]
        
print(max(max_dp), min(min_dp))
 