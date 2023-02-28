# # # import sys
# # # sys.setrecursionlimit(10 ** 5)


# # # n = int(input())
# # # nums = list(map(int, sys.stdin.readline().split()))

# # # nums.sort()
# # # m = nums.pop()

# # # k = (n-1)//2

# # # ans = [m]
# # # print(nums)

# # # if not (n-1)%2:
# # #     large = nums[k+1:]
# # #     small = nums[:k+1]
# # # else:
# # #     large = nums[k+1:]
# # #     small = nums[:k+1]
# # # small.sort(reverse=True)
# # # print(small, large)

# # # #   -1 3 0 2

# # # while True:
# # #     if not small and not large:
# # #         break
    
# # #     if len(small) == 1:
# # #         ans = [small.pop()] + ans
# # #         one = True
# # #     else:
# # #         ans = [small.pop()] + ans + [small.pop()]
# # #         one = False
        
# # #     if not small and not large:
# # #         break
    
# # #     if len(large) == 1:
# # #         if one:
# # #             ans =  ans + [large.pop()] 
# # #         else:
# # #             ans = [large.pop()] + ans
# # #     elif len(large) == 2:
        
# # #     else:
# # #         ans = [large.pop()] + ans + [large.pop()]

# # # print(ans)
# # # total = 0
# # # for i in range(n-1):
# # #     total += abs(ans[i]-ans[i+1])

# # # print(total)
    
        


# # import sys
# # sys.setrecursionlimit(10 ** 5)


# # n = int(input())
# # nums = list(map(int, sys.stdin.readline().split()))

# # visited = []
# # max_total = 0 

# # def BT():
# #     global max_total
    
# #     if len(visited) == n:
# #         total = 0
# #         # visited = [2,1,0,3,4]
# #         for i in range(n-1):
# #             total += abs(nums[visited[i]]-nums[visited[i+1]])
# #         if total > max_total:
# #             max_total = total 
# #         return
    
    
# #     for i in range(n):
# #         if i not in visited:
# #             visited.append(i)
# #             BT()
# #             visited.pop()
            
# # BT()
# # print(max_total)
        
# import sys
# from itertools import permutations

# input = sys.stdin.readline
# N = int(input())
# A = list(map(int, input().split()))

# cases = list(permutations(A))

# print(cases)

