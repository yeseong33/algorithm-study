import sys

a = 1
b = 1

while True:
    a, b = map(int, sys.stdin.readline().split())
    if a == 0 and b == 0:
        break
    c = 0
    for i in range(2, max(a, b)//2 +1):
        if a * i == b:
            print('factor')
            c += 1
            break
        elif b * i == a:
            print('multiple')
            c += 1
            break
    if c == 0:
        print('neither')

