nums = [0, 1, 1, 2, 3, 5]

def fi(n):
    for i in range(6, n+1):
        k = nums[i-2]+ nums[i-1]
        nums.append(k)
    return nums[n]


n = int(input())
print(fi(n))




# def fib(n):
#     if n > 1:
#         a, b = 0, 1
#         for _ in range(2, n+1):
#             a, b = b, a + b
#         return b
#     else:
#         return n