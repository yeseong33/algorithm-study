# # 1 5 2 1 4 3 4 5 2 1

# # 가장 앞에 있을 경우
# # 점점 작아지게 근데 가장 길게 
# # max랑 비교, 더 작을경우 

# # 9 5 6 5 3 4 2 1
# # 1 2 4 3 5 6 5 9


# # def counting(nums, count):
# #     n = len(nums)
# #     for i in range(n):
# #         for j in range(i):
# #             if nums[i] > nums[j]:
# #                 if count[i] < count[j] + 1:
# #                     count[i] = count[j] + 1
# #     return max(count)
                    

# import sys

# n = int(input())

# nums = list(map(int, sys.stdin.readline().split()))
# nums_copy = nums.copy()

# # 1 5 2 1 4 3 4 5 2 1

# ans = []

# # maximum = max(nums)
# # k = nums.count(maximum)
# # idx = []
# # idx.append(nums_copy.index(maximum))
# # nums_copy.remove(maximum)
# # for i in range(k-1):
# #     idx.append(nums_copy.index(maximum)+1+i)
# #     nums_copy.remove(maximum)
    
# # idx = [1, 7]


# for i in range(n):
#     rise = nums[:i+1].copy()
#     decrease = nums[i:].copy()
#     # 순서 반전 
#     decrease = decrease[::-1]

#     rise_count = [1] * len(rise)
#     decrease_count = [1] * len(decrease)

 
#     a = counting(rise, rise_count)
#     b = counting(decrease, decrease_count)
#     ans.append(a+b-1)
    
# print(max(ans))


import sys

n = int(input())
nums = list(map(int, sys.stdin.readline().split()))
nums_reverse = nums[::-1]
# count = [[1, 1] for i in range(n)]
count = [1]* n
count_r = [1] * n
print(count)

for i in range(n):
    for j in range(i):
        if nums[i] > nums[j]:
            if count[i] < count[j] + 1:
                 count[i] = count[j] + 1

# for i in range(n-1, -1, -1):
#     for j in range(n-1, i+1, -1):
#         if nums[i] > nums[j]:
#             if count[i][1] < count[j][1] + 1:
#                  count[i][1] = count[j][1] + 1

for i in range(n):
    for j in range(i):
        if nums_reverse[i] > nums_reverse[j]:
            if count_r[i] < count_r[j] + 1:
                 count_r[i] = count_r[j] + 1

count_r = count_r[::-1]

ans = []
for i in range(n):
    k = count[i] + count_r[i]
    ans.append(k-1)
print(ans)
print(max(ans))
# print(count)
# ans = []
# for i in count:
#     a = i[0]
#     b = i[1]
#     ans.append(a+b)
# print(ans)
# print(max(ans))
                 
# 1 5 2 1 4 3 4 5 2 1
# 1 2 5 4 3 4 1 2 5 1 