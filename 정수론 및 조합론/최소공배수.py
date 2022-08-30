import sys

n = int(sys.stdin.readline())



a = 10
b = 6

if a < b:
    a, b = b, a
for i in range(a, a*b+1 , a):
    for j in range(b, a*b+1, b):
        if i == j:
            print(i)
            break
        elif i < j:
            break 
    if i == j:
        break               


# for i in range(n):
#     a, b = map(int, sys.stdin.readline().split())
#     print(max_co(a, b))
    

