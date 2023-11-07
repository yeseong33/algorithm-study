# -*- coding: utf-8 -*-
import sys
a = list(map(str, sys.stdin.readline().strip().split('-')))
print(a)
if len(a[1]) == 4 and len(a[2]) == 4:
    print('valid')
else:
    print('invalid')