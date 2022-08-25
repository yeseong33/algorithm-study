import sys

s = list(map(int, sys.stdin.readline().split()))

x, y, w, h = s


if w / 2 <= x:
    if h / 2 <= y:
        x_1 = w-x
        y_1 = h-y
        print(min(x_1, y_1))
    elif h / 2 > y:
        x_1 = w-x
        y_1 = y
        print(min(x_1, y_1))
else:
    if h / 2 <= y:
        x_1 = x
        y_1 = h-y
        print(min(x_1, y_1))
    else:
        print(min(x, y))
        
