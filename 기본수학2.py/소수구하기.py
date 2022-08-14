# import sys

# m, n = map(int, sys.stdin.readline().split())

# nums = [False, False] + [True] * n

# for i in range(2, int(n** 0.5)+1):
#     if nums[i]:
#         for j in range(i*i, n+1, i):
#             nums[j] = False
             
# for i in range(m, n+1):
#     if nums[i]:
#         print(i)


def SieveOfEratosthenes(n, m):
 
    prime = [True for i in range(n+1)]
    p = 2
    while (p * p <= n):
        if (prime[p] == True):
            for i in range(p * p, n+1, p):
                prime[i] = False
        p += 1
    for p in range(m, n+1):
        if prime[p]:
            print(p)

import sys

m, n = map(int, sys.stdin.readline().split())

SieveOfEratosthenes(n, m)