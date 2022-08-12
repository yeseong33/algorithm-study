import sys 

n = int(sys.stdin.readline())

# a = 0
# b = 2
# k = 0

# for i in range(n):
#     if a == 1 and b % 2 == 1:
#         b += 1
#         k = b
#     elif b == 1 and a % 2 == 0:
#         a += 1
#         k = a
#     else:
#         if k % 2 == 0:
#             a += 1
#             b -= 1
#         else:
#             a -= 1
#             b += 1        
# print(str(a) + '/' + str(b))

            

nums = 1
for i in range(n):
    if n / nums <= 1:
        if (i+1) % 2 == 1:
            num = nums % n + 1
            a = num
            b = (i+2) - a
            print(str(a) + '/'+ str(b))
            break
        else:
            num = nums % n + 1
            b = num
            a = (i+2) -b 
            print(str(a) + '/'+ str(b))
            break 
    nums += (i+2)
    