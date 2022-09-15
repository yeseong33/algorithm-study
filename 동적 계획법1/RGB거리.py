
# import sys

# n = int(input())
# nums = []
# cost = 0
# costs = []
# for i in range(n):
#     k = list(map(int, sys.stdin.readline().split()))
#     k += [1001]
#     nums.append(k)
    
# for i in range(3):
#     start = i
#     for j in range(n):
#         RGB = nums[j][:]
#         print(RGB)
#         if j == 0:
#             m = RGB[start]
#             idx = start
#             cost += m
#             continue
#         print(idx, 'idx')
#         RGB[idx] = 1001
#         m = min(RGB)
        
#         if RGB.count(m) == 2: 
#             idx = 3
#             cost += m
#             continue
        
#         idx = RGB.index(m)
#         cost += m
        
#     costs.append(cost)
#     cost = 0

# print(costs)
# print(min(costs))

# import sys

# n = int(input())

# nums = []
# costs = []
# idx = 3
# cost = 0

# for i in range(n):
#     k = list(map(int, sys.stdin.readline().split()))
#     k += [1001]
#     nums.append(k)

# for i in range(3):
#     start = i
#     for j in range(n):
#         RGB = nums[j][:]
#         RGB[idx] = 1001
        
#         if j == 0:
#             m = RGB[start]
#             idx = start
#             cost += m
#             continue
            
#         m = min(RGB)
        
#         if RGB.count(m) == 2: 
#             a = m
#             b = m
#             RGB = nums[j][:]
            
#             if idx == 0:
#                 idx_a, idx_b =1, 2
#             elif idx == 1:
#                 idx_a, idx_b =0, 2
#             elif idx == 2:
#                 idx_a, idx_b =0, 1
                     
#             while True:
#                 a += RGB[idx_a]
#                 b += RGB[idx_b]
#                 j += 1
#                 if j > n:
#                     break
#                 RGB = nums[j][:]
#                 if RGB.index(min(RGB)) == idx:
                    
#                     break 
#                 idx_a, idx_b = idx_b, idx_a
                 
        
#         idx = RGB.index(m)
#         cost += m
#     costs.append(cost)
#     cost = 0
    
# print(costs)


import sys 

n = int(input())

idx = {0:[1, 2], 1:[0, 2], 2:[0, 1]}
k = [0, 0, 0]

for i in range(n):
    cost = list(map(int, sys.stdin.readline().split()))
    
    for j in range(3):
        cost[j] += min(k[idx[j][0]], k[idx[j][1]])
    k = cost

print(min(cost))


3
26 40 83

49 60 57

13 89 99

