import sys

n, m = map(int, sys.stdin.readline().split())
nums = list(map(int, sys.stdin.readline().split()))
temp = [0]
count = 0

for i in range(n):
    temp.append((nums[i]+temp[-1])%m)
    
# #     1 2 3 1 2 
# #   0 1 3 6 7 9
# #   0 1 0 0 1 0

k = dict()     
for i in temp[1:]:
    if i not in k:
        k[i] = 1
    else:
        k[i] += 1

# 조합
for i in k.values():
    count += i * (i-1)//2        

# 3 4
# 1 2 3
# 1 2 3 

if 0 in k:
    count += k[0]
print(count)



# for i in k.values():
#     p1 = 1
#     for j in range(1,i+1):
#         p1 *= j
#     p2 = 1
#     for j in range(1,i-1):
#         p2 *= j
#     count += p1 // (2 * p2)
# count += k[0]
# print(count)


# for i in range(1,len(temp)):
#     for j in range(i+1, len(temp)):
#         if temp[i] == temp[j]:
#             if temp[i] == 0:
#                 count += 2
#             else:
#                 count += 1         
    
