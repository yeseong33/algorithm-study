# def fac(n):
#     if n > 1:
#         return fac(n-1) * n
#     else:
#         return 1



# def fac(n):
#     def loop(n, k):
#         if n > 1:
#             return loop(n-1, k*n)
#         else:
#             return k
#     return loop(n, 1)


def fac(n):
    k = 1
    for i in range(1, n+1):
        k *= i
    return k

n = int(input())

print(fac(n))  


