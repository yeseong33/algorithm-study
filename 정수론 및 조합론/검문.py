# # import sys, math 

# # n = int(sys.stdin.readline())

# # nums = [int(sys.stdin.readline()) for i in range(n)]

# # # ## (1) 
# # m = []
# # a = 2
# # while a <= nums[1]-nums[0]:
# #     c = 0 
           
# #     t = nums[0] % a

# #     for i in nums:
# #         if t != i % a:
# #             c += 1
# #             break
# #     if c == 0:
# #         m.append(a)
    
# #     a += 1
    
# # for i in m:
# #     print(i, end = ' ')




# ## (2)
# def make(n):
#     k = []
#     for i in range(1, int(n**(1/2))+1):
#         if n % i == 0:
#             k.append(i)
#             if i**2 != n:
#                 k.append(n//i)
#     k.sort()            
#     return k
# print(make(12))




# # mi = []
# # for i in range(len(nums)-1):
# #     k = nums[i+1]-nums[i]
# #     mi.append(k)


# # t = set(make(mi[0]))
# # for i in mi:
# #     k = t.intersection(set(make(i)))
# #     t = k


# # for i in t:
# #     print(i, end = ' ')


import sys, math 


def make(n):
    k = []
    for i in range(2, int(math.sqrt(n))+1):
        if n % i == 0:
            k.append(i)
            if i**2 != n:
                k.append(n//i)
    k.sort()
    k.append(n)            
    return k



print(make(25))
n = int(sys.stdin.readline())

nums = [int(sys.stdin.readline()) for i in range(n)]
nums.sort()

mi = []
for i in range(n-1):
    k = nums[i+1]-nums[i]
    mi.append(k)
print(mi)

t = set(make(mi[0]))
for i in mi:
    k = t.intersection(set(make(i)))
    t = k
t = list(t)
t.sort()

for i in t:
    print(i, end = ' ')
    
    
# 2

# 8

# 4
#  2 4
# 12