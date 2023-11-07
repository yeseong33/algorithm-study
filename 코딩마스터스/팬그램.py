# -*- coding: utf-8 -*-
import sys

a = sys.stdin.readline().strip()
a = a.lower()
alh = [0] * 26
for i in a:
    alh[ord(i)-97] = 1

if all(alh):
    print('YES')
else:
    print('NO')
