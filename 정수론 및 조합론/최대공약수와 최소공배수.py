# import sys


# # 1 2 3 4 6 8 12 24
# # 1 2 3 6 9 18

# def make(n):
#     nums = [1]
#     for i in range(2, n):
#         for j in range(i, n):
#             if i * j > n :
#                 break
#             elif i * j == n and i == j:
#                 nums.append(i)
#             elif i * j == n:
#                 nums.append(i)
#                 nums.append(j)
#     nums.append(n)
#     nums.sort()
#     return nums

# def max_co(a, b):
#     for i in range(len(a)-2, -1, -1):
#         if a[i] in b:
#             return a[i]

# def min_co(a, b):
#     for i in range(a, a*b+1, a):
#         for j in range(b, a*b+1, b):
#             if i == j:
#                 return i
#             elif j > i:
#                 break

# a, b = map(int, sys.stdin.readline().split())

# a_nums = make(a)
# b_nums = make(b)

# print(max_co(a_nums, b_nums))
# print(min_co(a, b))


