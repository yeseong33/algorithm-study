# count = 0
# def one(n, k):
#     global count
#     if n > 1:
#         if n % k == 0:
#             count += 1
#             return one(n//k, k)
#         else:
#             count += 1
#             return one(n-1, k)
#     else:
#         return count
# # print(one(17, 4))
# print(one(25, 5))


def one(n, k):
    c = 0
    while n != 1:
        if n % k == 0:
            n = n//k
        else:
            n = n-1
        c += 1
    return c
print(one(25, 5))

