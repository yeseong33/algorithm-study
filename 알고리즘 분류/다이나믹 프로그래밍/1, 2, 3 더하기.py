import sys

t = int(input())
memo = [0, 1, 2, 4] + [0] * 8

# # 5 , 2
# def ncn(a, b):
#     diff = a-b
#     small = min(diff, b)
#     bigger = max(diff, b)
#     k1 = 1
#     for i in range(a, bigger, -1):
#         k1 *= i
#     k2 = 1
#     for i in range(1, small+1):
#         k2 *= i
#     return int(k1 / k2)




t = int(input())
memo = [0, 1, 2, 4] + [0] * 8


def dp(n):
    if n == 1:
        return memo[1]
    elif n == 2:
        return memo[2]
    elif n == 3:
        return memo[3]
    else:
        memo[n] = dp(n-1) + dp(n-2) + dp(n-3)
        return memo[n]



for i in range(t):
    
    n = int(input())
    print(dp(n))
    
    



    
    
    
    
        
    