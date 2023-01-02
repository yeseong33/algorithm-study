import sys

n = int(sys.stdin.readline())

s = [sys.stdin.readline() for i in range(n)]

s = list(set(s))

s.sort(key= lambda x: (len(x), x) )

print(''.join(s))