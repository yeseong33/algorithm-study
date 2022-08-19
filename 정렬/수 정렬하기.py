import sys

n = int(sys.stdin.readline())

a = []
for i in range(n):
    num = int(sys.stdin.readline().strip())
    a.append(num)
a.sort()


for i in a:
    print(i)
    