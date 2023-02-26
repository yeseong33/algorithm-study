# # # 길이 갈리는 순간 다른 리스트를 저장 할 것임
# # import sys

# # m, n = map(int, sys.stdin.readline().split())

# # road = []

# # for i in range(m):
# #     k = list(map(int, sys.stdin.readline().split()))
# #     road.append(k)

# # ans = []
# # ans.append([[road[0][0]], 0, 0])
# # count = 0 

# # if n == 1 and m == 1:
# #     print(1)
# # else:

# #     while ans:
# #         h, x, y = ans.pop()
        
# #         if len(h) > 1 and h[-1] == road[m-1][n-1]:
# #             count +=1
# #             continue
        
# #         if x-1 >= 0 and road[x-1][y] < h[-1]:
# #             k = [h + [road[x-1][y]], x-1, y]
# #             if k not in ans:
# #                 ans.append(k)
# #             else:
# #                 count += 1
# #         if  x+1 < m and road[x+1][y]  < h[-1]:
# #             k = [h + [road[x+1][y] ], x+1, y]
# #             if k not in ans:
# #                 ans.append(k)
# #             else:
# #                 count += 1
# #         if  y+1 < n and road[x][y+1] < h[-1]:
# #             k =  [h + [road[x][y+1]], x, y+1]
# #             if k not in ans:
# #                 ans.append(k)
# #             else:
# #                 count += 1
# #         if y-1 >= 0 and road[x][y-1] < h[-1]:
# #             k = [h + [road[x][y-1]], x, y-1]
# #             if k not in ans:
# #                 ans.append(k)
# #             else:
# #                 count += 1
# #         # print(ans)
# #     print(count)
# 4 4
# 16 9 8 1
# 15 10 7 2
# 14 11 6 3
# 13 12 5 4


# import sys

# m, n = map(int, sys.stdin.readline().split())

# road = []

# for i in range(m):
#     k = list(map(int, sys.stdin.readline().split()))
#     road.append(k)
# ans = set()
# ans.add((road[0][0], 0, 0, 1))
# D = [(1, 0), (-1, 0), (0, 1), (0, -1)]
# count = 0 
# if n == 1 and m == 1:
#     print(1)
# else:

#     while ans:
#         temp = set()
#         for t in ans:
#             key, x, y, idc = t
            
#             if x != 0 and y != 0 and key == road[m-1][n-1]:
#                 count += idc
#                 print(idc, 'd')
#                 continue
            
#             for i in range(4):
#                 nx = x+D[i][0]
#                 ny = y+D[i][1]
                
#                 if ny < 0 or ny >= n or  nx < 0 or nx >= m:
#                     continue
#                 r = road[nx][ny]
#                 if r < key:
#                     cap = (r, nx, ny, idc)
#                     if cap not in temp:
#                         temp.add(cap)
#                     else:
#                         temp.remove(cap)
#                         cap = (r, nx, ny, idc+1)
#                         temp.add(cap)
#                         print(cap)
#                     #     print(cap)
#                     #     print(temp)
#                     #     count += 1
#         ans = temp.copy()
        

            
#     print(int(count))


# import sys

# m, n = map(int, sys.stdin.readline().split())

# road = []
# ans = [[0] * n for i in range(m)]
# ans[0][0] = 1
# print(ans)

# for i in range(m):
#     k = list(map(int, sys.stdin.readline().split()))
#     road.append(k)

# D = [(1, 0), (-1, 0), (0, 1), (0, -1)]

# box = set()
# box.add((0, 0))
# count = 0 

# while box:
#     temp = set()
#     for i in box:
#         x, y = i
#         key = road[x][y]
#         ans_key = ans[x][y]
        
#         if x == m and y ==n:
#             continue
        
#         for j in range(4):
#             nx = x + D[j][0]
#             ny = y + D[j][1]
            
#             if ny < 0 or ny >= n or  nx < 0 or nx >= m:
#                 continue
#             now = road[nx][ny]
#             ans_now = ans[nx][ny]
#             if key > now:
#                 ans[nx][ny] = ans[nx][ny] + ans[x][y]
#                 temp.add((nx, ny))
                
#     box = temp.copy()
    
# ans[1][1] = 2
# print(count)
# print(ans)
# [[1, 1, 1, 1, 1], 
#  [1, 2, 0, 2, 1], 
#  [1, 0, 0, 3, 0], 
#  [1, 1, 1, 5, 7]]
# [[1, 1, 1, 1, 1], 
#  [1, 0, 0, 1, 1], 
#  [1, 0, 0, 1, 0], 
#  [1, 1, 1, 2, 3]]

# [[1, 1, 1, 1, 1], 
#  [1, 0, 0, 1, 1], 
#  [1, 0, 0, 1, 1], 
#  [1, 1, 1, 2, 3]]


# [[1, 1, 1, 1], 
#  [0, 0, 0, 0], 
#  [0, 0, 0, 0], 
#  [0, 0, 0, 0]]
# 4 4 
# 16 9 8 1
# 15 10 7 2
# 14 11 6 3
# 13 12 5 4

import sys

m, n = map(int, sys.stdin.readline().split())

road = []
ans = [[-1] * n for i in range(m)]


for i in range(m):
    k = list(map(int, sys.stdin.readline().split()))
    road.append(k)

D = [(1, 0), (-1, 0), (0, 1), (0, -1)]


def dfs(ans, road, x, y):
    if x == m-1 and y == n-1:
        ans[m-1][n-1] = 1
        return
    if ans[x][y] != -1:
        return
    ans[x][y] = 0    
    
    for dx, dy in D:
        nx = x + dx      
        ny = y + dy
        if 0 <= nx < m and 0 <= ny < n:
            if road[x][y] > road[nx][ny]:
                dfs(ans, road, nx, ny)
                ans[x][y] += ans[nx][ny]
                
dfs(ans, road, 0, 0)
print(ans[0][0])