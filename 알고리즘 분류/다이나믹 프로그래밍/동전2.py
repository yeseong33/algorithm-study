# import sys

# n, k = map(int, sys.stdin.readline().split())

# coin = [int(sys.stdin.readline()) for i in range(n)]

# coin_count = [[0] * (k+1) for _ in range(n)] 

# count = 0 
# for i in range(n):
#     value = coin[i]
#     for j in range(value, k+1):
#         if j%value == 0:
#             coin_count[i][j] = j//value    
            
# result = [11000] * (k+1)
# # result[0] = 0

# for j in range(1, k+1):
#     for i in range(n):
#         if not coin_count[i][j]:
#             continue
        
#         if coin_count[i][j] < result[j]:
#             result[j] = coin_count[i][j]

# euu = 11000

# for i in range(1, k+1):
#     if i == k:
#         t = result[-1]
#     else:
#         t = result[i] + result[k-i]
#     if t < euu:
#         euu = t
        
# if euu == 11000:
#     print(-1)
# else:
#     print(euu)

# # [10001, 1, 2, 3, 4, 1, 6, 7, 8, 9, 2, 11, 1, 13, 14, 3]


# # [[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15], 
# #  [0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 2, 0, 0, 0, 0, 3], 
# #  [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0]]

# # 3 12
# # 10
# # 4
# # 2
# 3 12
# 10
# 4
# 2

import sys

n, k = map(int, sys.stdin.readline().split())

coins = [int(sys.stdin.readline()) for i in range(n)]
coins.sort()
dp = [0] * (k+1)

for coin in coins:
    for i in range(coin, k+1):
        if i % coin == 0:
            if dp[i] == 0:
                dp[i] = i//coin
            else:
                dp[i] = min(dp[i], i//coin)
        elif dp[i-coin] != 0:
            if dp[i] == 0:
                dp[i] = dp[i-coin] + 1
            else:
                dp[i] = min(dp[i], dp[i-coin] + 1 )

if not dp[-1]:
    print(-1)
else:
    print(dp[-1])