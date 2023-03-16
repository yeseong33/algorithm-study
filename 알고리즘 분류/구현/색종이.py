import sys

n = int(input())

paper = []

white = [[0] * 100 for i in range(100)]


def check(x, y):
    for i in range(10):
        for j in range(10):
            white[x+i][y+j] = 1


for i in range(n):
    a, b = map(int, sys.stdin.readline().split())
    check(a, b)

count = 0 

for i in white:
    count += sum(i)
print(count)
