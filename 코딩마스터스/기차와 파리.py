import sys
from math import floor

x, y, z = map(int, sys.stdin.readline().split())

k = (z * x) / (2*y)
print(floor(k))