import sys

n = int(input())

paper = []

white = [[0] * 100 for i in range(100)]


def check(x, y):
    for i in range(10):
        for j in range(10):
            if not white[x+i][y+j]:
                white[x+i][y+j] = 1


for i in range(n):
    a, b = map(int, sys.stdin.readline().split())
    check(a, b)

count = 0 

for i in range(100):
    for j in range(100):
        if not white[i][j]:
            count += 1
            
print(100 * 100 - count)
