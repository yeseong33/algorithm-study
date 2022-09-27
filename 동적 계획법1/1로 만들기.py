# # 10 5 4 2 1 4
# # 10 9 3 1 3  

# # [10, 10, 10]
# # [9, 5, 10]
# # [3, 8, 9], [4, 5, 5]
# # [1, 4]

# # [K] * 3 + [K]*3 +[K]+ 3
# n = int(input())
# nums = [n]
# tmp = []
# c = 0

# while 1 not in nums:
#     for i in range(len(nums)):
#         if nums[i] % 3 == 0 and nums[i]%3 not in tmp:
#             tmp.append(nums[i]//3)
#         if nums[i] % 2 == 0 and nums[i]%2 not in tmp:
#             tmp.append(nums[i]//2)
#         if nums[i]-1 not in tmp:
#             tmp.append(nums[i]-1)
#     nums = tmp
#     tmp = []
#     c += 1
# print(c)



n = int(input())
nums = set()
nums.add(n)
tmp = set()
c = 0


while 1 not in nums:
    for i in nums:
        if i % 3 == 0:
            tmp.add(i//3)
        if i % 2 == 0:
            tmp.add(i//2)
        if i-1 not in tmp and i-1 > 0:
            tmp.add(i-1)
    nums = tmp.copy()
    tmp = set()
    c += 1
    
print(c)

        
                