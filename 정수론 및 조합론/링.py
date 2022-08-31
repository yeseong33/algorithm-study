import sys
from fractions import Fraction

n = int(sys.stdin.readline())

rings = list(map(int, sys.stdin.readline().split()))

f = rings[0]

for i in rings[1:]:
    if (f/i).is_integer():
        print(f//i, '/', 1, sep = '')
    else:
        print(Fraction(f, i))
        
        
    