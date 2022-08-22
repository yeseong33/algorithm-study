# # 1) 
# import sys

# n = int(sys.stdin.readline())

# ans = [0] * n

# x = list(map(int, sys.stdin.readline().split()))
# x_remove = x.copy()


# for _ in range(n):
#     m = min(x_remove) 
#     # [2, 4, -10, 4, -9]
#     # [1000, 999, 1000, 999, 1000, 999]
#     for i in range(n):
#         if x[i] > m and x.count(m) == 1:
#             ans[i] += 1 
#             #[1, 0, 0, 0, 0]
#         elif x[i] > m and x.count(m) != 1:
#             nums = x.count(m)
#             ans[i] += 1/nums
#             # x = [1000, 999, 1000, 999, 1000, 999]
#             # ans = [1/3, 0, 1/3, 0, 1/3, 0]
#             # ans = [2/3, 0, 2/3, 0, 2/3, 0]
#             # ans = [3/3, 0, 3/3, 0, 3/3, 0]
#     x_remove.remove(m) 
#     # [2, 4, 4, -9]


# for i in range(n):
#     print(int(ans[i]), end=' ')




# 2) 
import sys

n = int(sys.stdin.readline())

ans = [0] * n


x = list(map(int, sys.stdin.readline().split()))
x_c = x.copy()
x_d = {}
for i in x:
    x_d[i] = 0
print(x_d)



x = list(set(x))
x.sort()


for i in range(len(x)):
    x_d[x[i]] = i
    
    
for i in range(n):
    print(x_d[x_c[i]], end = ' ')



