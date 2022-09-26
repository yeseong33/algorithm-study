# n = int(input())

# nums = [0] * 100
# nums[0] = 9
# nums[1] = 17
# # tmp = [1, 2, 3, 4, 5, 6, 7, 8, 9]
# # tmp = [10, 12, 21, 23, 32, 34, 43, 45, 54, 56, 65, 67, 76, 78, 87, 89, 98]
# tmp = [1, 1, 2, 2, 3, 3, 4, 4, 5, 5, 6, 6, 7, 7, 8, 8, 9]
# ans = []


# if n == 1:
#     print(9)
# elif n == 2:
#     print(17)
# else:
#     for i in range(2, n):
#         for j in tmp:
#             a = j + 1
#             b = j - 1
#             if a <= 9:
#                 ans.append(a)
#             if b > 0:
#                 ans.append(b)
#         tmp = ans
#         nums[i] = len(tmp) + nums[i-0]*9
#         ans = []
          
#     print(nums[n-1])
    
# use dict
n = int(input())
tmp = [0,1,1,1,1,1,1,1,1,1]
ans = [0,0,0,0,0,0,0,0,0,0]

for i in range(1, n):
    for j in range(10):
        if j == 0:
            ans[1] += tmp[j]
        elif j == 9:
            ans[8] += tmp[j]
        else:
            ans[j-1] += tmp[j]
            ans[j+1] += tmp[j]
    tmp = ans.copy()
    ans = [0] * 10
print(sum(tmp)%1000000000)


# tmp = {1:2, 2:2, 3:2, 4:2, 5:2, 6:2, 7:2, 8:2, 9:1}
# print(sum(tmp.values()))

# use n
# nums = [0] * 100
# nums[0] = 9
# nums[1] = 17


# for i in range(2, n):
#     nums[i-1]
#     nums[i] = nums[i-2] + nums[i-1]


