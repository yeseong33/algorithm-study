import sys

a, b = map(str, sys.stdin.readline().split())

a = a[-1::-1]
b = b[-1::-1]

if a > b:
    print(a)
else:
    print(b)
    