# # import sys
# # sys.setrecursionlimit(1010)
# # input = sys.stdin.readline


# # n = int(input())
# # nums =  list(map(int, input().split()))

# # nums_sum = [0]
# # total = 0 
# # for i in nums:
# #     total += i
# #     nums_sum.append(total) 

# # ans = -1
# # path = []
# # def dfs(idx, c, a, b):
# #     global ans
    
# #     if ans != -1 and  ans > nums_sum[n] - nums_sum[idx] + abs(a-b):
# #         return 

# #     if idx == n:
# #         if ans < abs(a-b):
# #             ans = abs(a-b)
# #         return
    
# #     for i in range(1, 4):
# #         idx_i = idx+i
# #         if idx_i <= n:
# #             now = nums_sum[idx_i] - nums_sum[idx]
# #             if c % 2:
# #                 dfs(idx_i, c+1, a+now, b)
# #             else:
# #                 dfs(idx_i, c+1, a, b+now)

# # dfs(0, 0, 0, 0)
# # print(ans)

# import sys
# input = sys.stdin.readline


# n = int(input())
# nums =  list(map(int, input().split()))

# nums_sum = [0]
# total = 0 
# for i in nums:
#     total += i
#     nums_sum.append(total) 

# ans = 0 
# for mode in range(2):
#     idx = 0
#     total = 0   
#     if mode == 1:
#         min_t = 200
#         tmp_idx = 0 
#         if n <= 3 :
#             continue
#         for i in range(1, 4):
#             now = nums_sum[idx+i] - nums_sum[idx]
#             if min_t > now:
#                 min_t = now
#                 tmp_idx = i
#         total -= min_t
#         idx += tmp_idx
#     while True:
#         k =0 
#         if n-idx <= 3:
#             total += nums_sum[n]-nums_sum[idx]
#             break
#         elif n-idx < 6:
#             k = 6 -(n-idx)
#         print(k)
#         tmp_al = []
#         min_tmp = 1000000000000
#         tmp = []
#         max_tmp = 0
#         for i in range(1, 4):
#             front = nums_sum[idx+i] - nums_sum[idx]
#             for j in range(1, 4-k):
#                 back = nums_sum[idx+i+j] - nums_sum[idx+i]
#                 expec = (front - back +nums_sum[idx+i+j]-nums_sum[idx])
#                 if expec < min_tmp:
#                     min_tmp = expec
#                     tmp_al = (i, j)
#                 if front - back > max_tmp:
#                     max_tmp = front - back
#                     tmp = (i, j)
        
#         total +=  nums_sum[idx+tmp_al[0]] - nums_sum[idx] - (nums_sum[idx+tmp_al[0]+tmp_al[1]] - nums_sum[idx+tmp_al[0]])

#         idx += tmp[0] + tmp[1]
#     if ans < total:
#         ans = total
# print(ans)


from itertools import product

def find_combinations_with_sum(numbers, target_sum):
    result = []
    for r in range(1, target_sum + 1):
        for combo in product(numbers, repeat=r):
            print(combo)
            if sum(combo) == target_sum:
                result.append(combo)
    return result

# 예시
numbers = [1, 2, 3]
target_sum = 10
result = find_combinations_with_sum(numbers, target_sum)
print(result)







# def max_score_difference(n, cards):
#     max_difference = float('-inf')

#     # 가능한 모든 뽑는 순서에 대해 반복
#     for order in permutations(cards):
#         print(order)
#         # odd_order = order[:n]  # 홀수 순서
#         # even_order = order[n:]  # 짝수 순서

#         # odd_score = sum(odd_order)
#         # even_score = sum(even_order)

#         # difference = abs(odd_score - even_score)
#         # max_difference = max(max_difference, difference)
#     for combo in combinations(cards):
#         print(combo)
#     return max_difference

# # 예시
# n = 5
# cards = [1, 2, 3 , 4, 5]
# result = max_score_difference(n, cards)
# print(result)