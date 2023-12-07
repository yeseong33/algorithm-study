import sys
from collections import Counter


n = int(sys.stdin.readline())
ans = bin(n)
count = Counter(ans[2:])
print(count['1'])