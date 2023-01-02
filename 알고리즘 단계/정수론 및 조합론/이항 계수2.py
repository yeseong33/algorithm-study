import sys


## (1)
def fac(s):
    t = 1
    while s != 0:
        t *= s
        s -= 1
    return t
    

n, k = map(int, sys.stdin.readline().split())


if 0 <= k <= n:
    print(int(fac(n)//(fac(k)*fac(n-k)) % 10007))
else:
    print(0)



## (2)

n, k = map(int, sys.stdin.readline().split())

p1 = 1
for i in range(1, n+1):
    p1 *= i

p2 = 1
for i in range(1, n-k+1):
    p2 *= i

p3 = 1
for i in range(1, k+1):
    p3 *= i

print(int(p1//(p2*p3) % 10007))