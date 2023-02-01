# import sys

# n = int(input())

# reserve = [[0,0]]
# visited = []
# price = 0
# ans = 0
# idx = 1

# for i in range(n):
#     t, p = map(int, sys.stdin.readline().split())
#     reserve.append([t, p])

# def dfs():
#     global idx, ans
#     temp =idx
    
    
#     if visited != [] and visited[-1] > n:
#         total = 0
#         for i in visited:
#             if i < n and i + reserve[i][0] <= n+1:
#                 total += reserve[i][1]
#             elif i == n:
#                 if reserve[i][0] == 1:
#                     total += reserve[i][1]
        
#         if total > ans:
#             ans = total
            
#     else:
#           for i in range(1, n+6):
#             if visited == [] or i >= visited[-1]+ reserve[visited[-1]][0]:
#                 visited.append(i)
#                 idx = i
#                 dfs()
#                 visited.pop()
#                 idx = temp

# dfs()
# print(ans)

# import cProfile

# cProfile.run("dfs()")



import sys

n = int(input())

reserve = [[0,0]]
money = []
total = []

for i in range(n):
    t, p = map(int, sys.stdin.readline().split())
    reserve.append([t, p])


dp = [0] * (n+1)
 
for i in range(n):
    for j in range(i+reserve[i][0], n+1):
        print(dp)
        if dp[j] < dp[i] + reserve[i][1]:
            dp[j] = dp[i] + reserve[i][1]
print(dp)
