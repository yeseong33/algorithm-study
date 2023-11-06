# -*- coding: utf-8 -*-
import sys

n, k = map(int, sys.stdin.readline().split( ))
alphas = sys.stdin.readline().strip()
ans = ''
for i in alphas:
    ans += i * k
print(ans)
