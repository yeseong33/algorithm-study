# 여러개가 필요한 경우가 쟁점
# 백트래킹으로 풀어 보려 했으나 --> 시간초과
# import sys
# sys.setrecursionlimit(100000)
# total = 0
# count = 0 

# def back(idx):
#     global count, total
    
#     if total > k:
#         return 
#     if total == k:
#         count += 1
        
#     else:
#         for i in range(idx, n):
#             value = coin[i]
#             total += value
#             back(i)
#             total -= value
# back(0)
# print(count)

# import sys
# n, k = map(int, sys.stdin.readline().split())

# coin = [int(sys.stdin.readline()) for _ in range(n)]

# count = [[0] * (k+1) for i in range(n+1)]


# for i in range(1, n+1):
#     value = coin[i-1]
#     if value > k:
#         continue
    
#     for j in range(1, k+1):
        
#         if j%value == 0:
#             only = 1
#         else:
#             only = 0 
#         combi = 0 
        
#         if j == 10:
#             only += count[i-1][j]
            
#         for t in range(k-j, k, value):
#             combi += count[i-1][t]
        
#         count[i][j] = only + combi
        
#     # print(count)
# print(count[n][k])
   
# 1 1  
# 4 1,2
# 1 2

# 1 1 5

# 2 1 2 5

# 0 2 5

# 1 5 


# [[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], 
#  [0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], 
#  [0, 4, 5, 4, 5, 4, 5, 4, 5, 4, 6],
#  [0, 4, 4, 4, 4, 5, 4, 4, 4, 4, 11]]
# [[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], 
#  [0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
#  [0, 0, 1, 0, 2, 1, 3, 2, 4, 3, 6],
#  [0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 8]]



import sys
n, k = map(int, sys.stdin.readline().split())

coin = [int(sys.stdin.readline()) for _ in range(n)]

count = [0] * (k+1)
count[0] = 1 



for value in coin:
    for i in range(value, k+1):
        # if i-value >=0:
        count[i] += count[i- value] 
        print(count)
    
        
print(count)

# [[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],3
#  [0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], 
#  [0, 1, 2, 2, 3, 3, 4, 4, 5, 5, 6],
#  [0, 5, 5, 4, 4, 4, 8, 7, 6, 5, 10]]