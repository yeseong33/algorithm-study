# n = int(input())

# zz = n // 2

# c = 0


# for i in range(0, zz+1):
#     one = n - 2*i 

#     if i == 0 or one == 0:
#         c += 1
        
#     else:
#         n = one + i
#         r = min(one, i)
#         p1 = 1
#         for i in range(n+1-r, n+1):
#             p1 *= i
#         p2 = 1
#         for i in range(1, r+1):
#             p2 *= i
        
#         c += int(p1//p2)

        
# print(c%15746)
    

n = int(input())

a = 0
b = 1
for i in range(n):
    a, b = b , (a+b)%15746

print(b)

# 7364
# 3595