import sys

n = int(input())

def solution():
    s = 0
    for _ in range(n):
        string = sys.stdin.readline().strip()
        if string not in ['all', 'empty']:
            a, b = string.split()
            b = int(b)
        else:
            a = string
        if a == 'add':
            s |= 1<<b
        elif a == 'remove':
            s &= ~(1<<b)
        elif a == 'check':
            sys.stdout.write('1\n' if s & (1<<b) else '0\n')
        elif a == 'toggle':
            s ^= 1<< b
        elif a == 'all':
            s = int('1'*21, 2)
        else:
            s = 0
solution()
