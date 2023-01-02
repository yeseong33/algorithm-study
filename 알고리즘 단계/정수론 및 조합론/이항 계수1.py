import sys

def fac(n):
    if n > 1:
        return fac(n-1) * n 
    else:
        return 1

n, k = map(int, sys.stdin.readline().split())


if 0 <= k <= n:
    print(int(fac(n)/ (fac(k) * fac(n-k))))
else:
    print(0)
    