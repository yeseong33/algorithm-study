# -*- coding: utf-8 -*-
import sys

a = list(sys.stdin.readline().strip())
b = list(sys.stdin.readline().strip())
c = list(sys.stdin.readline().strip())

nums = a + b+c

result = []
def check(start, end):
    for k in range(start, end+1):
        nums = a + list(str(k)) + b + c
        nums = list(map(int, nums))

        A = 0
        B = 0 
        for i in range(0, 12):
            if i % 2 == 0:
                A += nums[i]
            else:
                B += nums[i]
        R = (2*B+A) % 10
        error_code = -1
        if 10 -R == 10:
            error_code = 0
        else:
            error_code = 10-R
            
        if error_code == nums[-1]:
            result.append('O')
            return
    result.append('X')

ranges = [(11, 15), (21, 22), (31, 51), (81, 86), (71, 71)]

for s, e in ranges:
    check(s, e)
print(''.join(result))
