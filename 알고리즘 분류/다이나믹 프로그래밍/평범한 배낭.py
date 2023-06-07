# # import sys

# # n, k = map(int, sys.stdin.readline().split())

# # bag = [0] + [0] * 10**5
# # max_w = 0
# # idx = []

# # for i in range(n):
# #     w, v = map(int, sys.stdin.readline().split())
# #     idx.append(w)
# #     if bag[w]:
# #         bag[2*w] = bag[w] + v
# #         if max_w <=2 * w <= k:
# #             max_w = 2 *w
        
# #     else:
# #         bag[w] = v
# #         if max_w <= w <= k:
# #             max_w = w
    
# # for i in range(1, max_w+1):
# #     if bag[i-1] > bag[i] and not bag[i]:
# #         bag[i] = bag[i-1]

# # wegiht = 0 
# # value = 0 
# # max_value = 0
# # idx.sort()
# # for i in range(n):
    
# #     wegiht += idx[i]
    
# #     if wegiht > k:
# #         if idx[i] < k:
# #             total = 0
# #             value = 0
# #             t = i
# #             while True:
# #                 total += idx[t]
# #                 if total > k:
# #                     break
# #                 value += bag[idx[t]]
# #                 t -= 1
# #         else:
# #             value = bag[k-idx[i]] + bag[idx[i]] 
# #     else:
# #         value += bag[idx[i]]
# #     if value >= max_value:
# #         max_value = value
# # print(max_value)

        
    
        
        
# 5 10
# 3 8
# 4 7
# 1 9
# 5 6
# 2 1

# 6 304
# 98 98
# 4 4
# 6 6
# 100 100
# 101 101
# 103 103

# import sys

# n, k = map(int, sys.stdin.readline().split())

# bag = [[0] * (k+1) for _ in range(n+1)]
# stuff = []

# for i in range(n):
#     w, v = map(int, sys.stdin.readline().split())
#     stuff.append([w, v])

# print(bag)

# for i in range(1, n+1):
#     w, v = stuff.pop()
#     for j in range(1, k+1):
#         if w > j:
#             bag[i][j] = bag[i-1][j]
#         else:
#             bag[i][j] = max(v+bag[i-1][j-w], bag[i-1][j])
# print(bag)

# [[0, 0, 0, 0, 0, 0, 0, 0],
#  [0, 0, 0, 0, 0, 12, 12, 12],
#  [0, 0, 0, 6, 6, 12, 12, 12],
#  [0, 0, 0, 6, 8, 12, 12, 14], 
#  [0, 0, 0, 6, 8, 12, 13, 14]]

# #          [[0, 1, 2, 3, 4, 5, 6, 7], 
# # 5 12      [0, 0, 0, 0, 0, 12, 12, 12], 
# # 3 6       [0, 0, 0, 6, 6, 6, 6, 6],
# # 4 8       [0, 0, 0, 6, 14, 14, 14, 14],
# # 6 13      [0, 0, 0, 6, 14, 14, 14, 14]]
# # w 1 2 3 4 5 6  7 
# # a 0 0 0 0 0 13 13 
# # b
# # c
# # d

import sys

n, k = map(int, sys.stdin.readline().split())
bag = [0] * (k+1)

for _ in range(n):
    w, v = map(int, sys.stdin.readline().split())

    # 이 부분을 range(1, K+1) 로 가정하면
    # 최대값을 구하는 것이기 때문에 한 물건에 대해 두 번 겹치는 상황이 올 수 있다.
    # 따라서, 최대값을 구하기 위해서는 bag 리스트를 맨 뒤에서부터 돌려 줘야 함(top-down)
    
    for i in range(k, 0, -1):
        if  w > i: continue
        bag[i] = max(v + bag[i-w], bag[i])
        print(bag)
print(bag[-1])

        