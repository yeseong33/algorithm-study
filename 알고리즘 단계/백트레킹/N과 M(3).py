import sys

n, m = map(int, sys.stdin.readline().split())

l = []

def d():
    if len(l) == m:
        print(' '.join(map(str, l)))
        return 
    else:
        for i in range(1, n+1):
            l.append(i)
            d()
            l.pop()

d()