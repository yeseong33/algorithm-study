# import sys

# n = int(input())
# nums = []

# for i in range(n):
#     k = list(map(int, sys.stdin.readline().split()))+ [-1] * (n-i-1)
#     nums.append(k)

# nums = nums[-1: :-1]
# print(nums)
# r = dict()
# for i in range(n):
#     r[1000*i + i] = nums[0][i]

# r_r = dict()

# for i in range(1, n):
#     for j in r.keys():

#         v = j % 1000
#         if v == 0:
#             r[j] += nums[i][v]
#             r_r[j] = r[j]
            
#         else:
#             a = nums[i][v]
#             b = nums[i][v-1]
#             r[j] += max(a, b)
            
#             if b > a:
#                 r_r[j-1] = r[j]
#             elif a == b:
#                 new = 1000*len(r)+v
#                 print(j)
#                 print('this')
                
#                 r_r[j] = r[j]
#                 r_r[new-1] = r[j]
                
#             else:
#                 r_r[j] = r[j]
#         print(r)
#         print(r_r)
#     r = r_r
#     r_r = dict()


# print(max(r.values()))
# print(r)

# r = dict()
# r[10] = 1
# r[100] = 2
# for i in r.keys():
#     print(i)


# 4
# 1
# 0 1
# 0 0 1
# 100 0 0 0
# 15
# 75
# 95 64
# 17 47 82
# 18 35 87 10
# 20 04 82 47 65
# 19 01 23 75 03 34
# 88 02 77 73 07 63 67
# 99 65 04 28 06 16 70 92
# 41 41 26 56 83 40 80 70 33
# 41 48 72 33 47 32 37 16 94 29
# 53 71 44 65 25 43 91 52 97 51 14
# 70 11 33 28 77 73 17 78 39 68 17 57
# 91 71 52 38 17 14 91 43 58 50 27 29 48
# 63 66 04 68 89 53 67 30 73 16 69 87 40 31
# 04 62 98 27 23 09 70 98 73 93 38 53 60 04 23

# n = int(input())
# arr = [list(map(int, input().split())) for _ in range(n)]
# dp = [[0]*(x+1) for x in range(n)]
# for i in range(n-1):
#     for j in range(len(arr[i])):
#         if i ==0 :
#             dp[i+1][j] = arr[i][j] + arr[i+1][j]
#             dp[i+1][j+1] = arr[i][j] + arr[i+1][j+1]
#         else:
#             if dp[i+1][j] < dp[i][j] + arr[i+1][j]:
#                 dp[i+1][j] = dp[i][j] + arr[i+1][j]
#             dp[i+1][j+1] = dp[i][j] + arr[i+1][j+1]
#     print(dp)

# if n == 1:
#     print(arr[0][0])
# else:
#     result = max(dp[n-1])
#     print(result)



# import sys

# n = int(input())
# nums = []

# for i in range(n):
#     k = list(map(int, sys.stdin.readline().split()))+ [-1] * (n-i-1)
#     nums.append(k)

# r = dict()
# r[0] = nums[0][0]
# print(r)
# r_r = dict()


# 7
# 3 8
# 8 1 0
# 2 7 4 4
# 4 5 2 6 5

# for i in range(1, n):
#     for j in r.keys():
#         v = j % 1000
        
#         r_r[1000*len(r_r)+j] = r[j] + nums[i][v]
#         r_r[1000*len(r_r)+j+1] = r[j] + nums[i][v+1]
        
#     print(r)
#     print(r_r)
#     r = r_r
#     r_r = dict()

# print(max(r.values()))



    