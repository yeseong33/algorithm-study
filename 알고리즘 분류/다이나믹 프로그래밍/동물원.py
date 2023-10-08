import sys

n = int(input())

a1 = 1
a2 = 3

for i in range(2, n+1):
    a3 = 2 * a2 + a1
    a1, a2 = a2, a3
    
print(a2%9901)