import sys

n = int(sys.stdin.readline())

c = [sys.stdin.readline() for i in range(n)]

c.sort(key = lambda x: (int(x.split()[0])) )

print(''.join(c))