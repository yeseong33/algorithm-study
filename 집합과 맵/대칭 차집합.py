import sys

a, b = map(int, sys.stdin.readline().split())

A = set(map(int,sys.stdin.readline().split()))
B = set(map(int,sys.stdin.readline().split()))


ans = []

for i in A:
    if i not in B:
        ans.append(i)

for i in B:
    if i not in A:
        ans.append(i)

print(len(ans))

