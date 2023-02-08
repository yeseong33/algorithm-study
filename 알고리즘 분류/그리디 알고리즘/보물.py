import sys


n = int(input())

A = list(map(int, sys.stdin.readline().split()))
B = list(map(int, sys.stdin.readline().split()))

A.sort()
B.sort(reverse=True)

ans = 0
for i in range(n):
    ans += A[i] * B[i]
print(ans)