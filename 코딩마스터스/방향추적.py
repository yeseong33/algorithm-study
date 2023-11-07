from sys import stdin as ss
from sys import stdout as so


ss = open('C:\\Users\\yeseong\\code\\algorithmstudy\\코딩마스터스\\input.txt')
print = so.write
# def run():
#     n = int(ss.readline())
#     x, y = map(int, ss.readline().split())

#     for _ in range(n-1):
#         nx, ny = map(int, ss.readline().split())
#         if x == nx:
#             if ny>y:
#                 d = 2
#                 dis = ny - y
#             else:
#                 d = 4
#                 dis = y - ny
#         else:
#             if nx>x:
#                 d = 1
#                 dis = nx - x
#             else:
#                 d = 3
#                 dis = x - nx
#         x, y = nx, ny
#         print(d, dis)
        
def run():
    n = int(ss.readline())
    x, y = map(int, ss.readline().split())
    k  =[]
    for _ in range(n - 1):
        nx, ny = map(int, ss.readline().split())
        dx, dy = nx - x, ny - y

        if dx == 0:
            d = 2 if dy > 0 else 4
            dis = abs(dy)
        else:
            d = 1 if dx > 0 else 3
            dis = abs(dx)

        x, y = nx, ny
        k.append((d, dis))
        
    for i in k:
        print(' '.join(map(str, i)) + '\n')

import cProfile

if __name__ == "__main__":
    cProfile.run("run()")

# import sys


# arr = [[1, 2], [2, 3], [3, 4]]
# for i in arr:
#     print(' '.join(map(str, i)) + '\n')