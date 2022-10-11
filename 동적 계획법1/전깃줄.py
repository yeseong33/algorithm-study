# import sys

# n = int(input())


# nums_a = []
# nums_b = []
# nums_c = []
# count = [0, 0, 0]
# ans = 0

# for i in range(n):
#     k = list(map(int,sys.stdin.readline().split()))
#     if k[0] < k[1]:
#         count[0] += 1
#         nums_a.append(k)
#     elif k[0] > k[1]:
#         count[1] += 1
#         nums_b.append(k)
#     else:
#         count[2] += 1
#         nums_c.append(k)

# nums_a.sort(key= lambda x: x[1])
# a2 = nums_a.copy()
# nums_b.sort(key= lambda x: x[1])
# b2 = nums_b.copy()
# nums_c.sort(key= lambda x: x[1])
# c2 = nums_c.copy()

# nums_a.sort(key= lambda x: x[0])
# a1 = nums_a.copy()
# nums_b.sort(key= lambda x: x[0])
# b1 = nums_b.copy()
# nums_c.sort(key= lambda x: x[0])
# c1 = nums_c.copy()


# count_copy = count.copy()

# for i in range(len(a1)):
#     for j in range(i):
#         if a1[i] != a2[j]



# if a1 != a2:
#     count_copy[0] = 0
# if b1 != b2:
#     count_copy[1] = 0
# if c1 != c2:
#     count_copy[2] = 0

# max_alpha = count.index(max(count_copy))
# print(count_copy)


# if nums_b == []:
#     nums_b.append([0,101])
# if nums_a == []:
#     nums_a.append([0,101])
# if nums_c == []:
#     nums_c.append([0,101])


# if max_alpha == 0:
#     for i in nums_b:
            
#         if i[0] < nums_a[0][0] and i[1] < nums_a[0][1] or i[0] > nums_a[-1][0] and i[1] > nums_a[-1][1]:          
#             ans += 1
#         else:
#             for j in range(1, len(nums_a)-1):
#                 if nums_a[j][0] < i[0] <nums_a[j+1][0] and nums_a[j][1] < i[1] <nums_a[j+1][1]:
#                     ans += 1

            
#     for i in nums_c:
#         if i[0] < nums_a[0][0] and i[1] < nums_a[0][1] or i[0] > nums_a[-1][0] and i[1] > nums_a[-1][1]:          
#             ans += 1
#         else:
#             for j in range(1, len(nums_a)-1):
#                 if nums_a[j][0] < i[0] <nums_a[j+1][0] and nums_a[j][1] < i[1] <nums_a[j+1][1]:
#                     ans += 1

# elif max_alpha == 1:
#     for i in nums_a:
#         if i[0] < nums_b[0][0] and i[1] < nums_b[0][1] or i[0] > nums_b[-1][0] and i[1] > nums_b[-1][1]:          
#             ans += 1
#         else:
#             for j in range(1, len(nums_b)-1):
#                 if nums_b[j][0] < i[0] <nums_b[j+1][0] and nums_b[j][1] < i[1] <nums_b[j+1][1]:
#                     ans += 1    
        
#     for i in nums_c:
#         if i[0] < nums_b[0][0] and i[1] < nums_b[0][1] or i[0] > nums_b[-1][0] and i[1] > nums_b[-1][1]:          
#             ans += 1
#         else:
#             for j in range(1, len(nums_b)-1):
#                 if nums_b[j][0] < i[0] <nums_b[j+1][0] and nums_b[j][1] < i[1] <nums_b[j+1][1]:
#                     ans += 1  
            
            
            
# elif max_alpha == 2:
#     for i in nums_a:
#         if i[0] < nums_c[0][0] and i[1] < nums_c[0][1] or i[0] > nums_c[-1][0] and i[1] > nums_c[-1][1]:          
#             ans += 1
#         else:
#             for j in range(1, len(nums_c)-1):
#                 if nums_c[j][0] < i[0] <nums_c[j+1][0] and nums_c[j][1] < i[1] <nums_c[j+1][1]:
#                     ans += 1  
#     for i in nums_b:
#         if i[0] < nums_c[0][0] and i[1] < nums_c[0][1] or i[0] > nums_c[-1][0] and i[1] > nums_c[-1][1]:          
#             ans += 1
#         else:
#             for j in range(1, len(nums_c)-1):
#                 if nums_c[j][0] < i[0] <nums_c[j+1][0] and nums_c[j][1] < i[1] <nums_c[j+1][1]:
#                     ans += 1



# print(sum(count))
# print(max(count_copy))
# print(ans)
# print(sum(count) - max(count_copy) - ans)


# import sys 

# n = int(input())

# nums = []

# for i in range(n):
#     k = list(map(int,sys.stdin.readline().split()))
#     nums.append(k)
    

# nums.sort(key = lambda x: x[0])

# count = []
# tmp = []

# for i in range(n):
#     t = 0
#     tmp = [nums[i]]
#     for j in range(i+1, n):
#         if nums[j][0] > nums[i][0] and nums[j][1] > nums[i][1]:
#             if             
#             t += 1 
#     count.append(t)

# c = max(count)

# print(n-c)



import sys

n = int(input())
nums = []
nums_1 = []
nums_2 = []

for i in range(n):
    k = list(map(int, sys.stdin.readline().split()))
    nums.append(k)
    
nums.sort(key = lambda x: x[0])

for i in range(n):
    nums_1.append(nums[i][0])
    nums_2.append(nums[i][1])



l = len(nums_2)
count = [1] * l
# answer
# 18 23 53 60 77 83 85
# 1  1  1  1  1  1  1  
# 10 20 10 30 20 50
# 1  2  1  3  2   4 

for i in range(l):
    for j in range(i):
        if nums_2[i] > nums_2[j]:
            if count[i] < count[j] + 1:
                 count[i] = count[j] + 1

c = max(count)

print(n-c)


            

