# c > a + b
import sys

a, b, c = list(map(int, sys.stdin.readline().split()))
count = 0 

if c <= b:
    k = -1
else:
    k = a // (c-b) +1
    
print(k)