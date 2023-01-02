import sys

n = int(sys.stdin.readline())

for i in range(n):
    n, m = map(int, sys.stdin.readline().split())
    if n == m:
        print(1)
        continue

    p1 = 1
    for i in range(1, n+1):
        p1 *= i
    
                
    p2 = 1
    for i in range(1, m+1):
        p2 *= i
    
    p3 = 1
    for i in range(1, m-n+1):
        p3 *= i
    
    
    k = p2 // (p1 * p3)
    print(k)    
