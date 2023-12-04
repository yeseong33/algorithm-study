import sys
input = sys.stdin.readline
for i in range(3):
    if i == 1:
        t = input()
        if t[1] != '0':
            print('impossible')
        else:
            print('possible')
    else:
        input()
