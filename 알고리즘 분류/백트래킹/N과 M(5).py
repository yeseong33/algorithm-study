# # import sys

# # n, m = map(int, sys.stdin.readline().split())

# # nums = list(map(int, sys.stdin.readline().split()))

# # nums.sort()
# # stack = []


# # def BT():
# #     global stack
    
# #     if len(stack) == m:
# #         print(*stack)
    
    
# #     else:
# #         for i in range(n):
# #             if nums[i] not in stack:
# #                 stack.append(nums[i])
# #                 BT()
# #                 stack.pop()
# # BT()


# import sys

# n, m = map(int, sys.stdin.readline().split())

# nums = list(map(int, sys.stdin.readline().split()))

# nums.sort()

# visited = [False] * n

# stack = []


# def BT(count):
    
#     if count == m:
#         print(*stack)
    
#     # if visited[idx]:
#     #     BT(idx, count+1)
        
    
#     for i in range(n):
#         if visited[i]:
#             continue
#         visited[i] = True
#         stack.append(nums[i])
#         BT(count+1)
#         visited[i] = False
#         stack.pop()
        
# BT(0)            
import sys

li = [[1,5,3],[2,5,7],[5,3,5]]
chk = [False]*3
m = sys.maxsize

def backtracking(row, score):
	if row == 4: # 재귀함수를 마치는 조건
		if score < m:
			return
	for i in range(1,4):
		if chk[i] == False : # 백트래킹에서의 한정조건
			chk[i] = True
			backtracking(row+1, score + li[row][i])
			chk[i] = False 
	return 

backtracking(1,0)
print(m)