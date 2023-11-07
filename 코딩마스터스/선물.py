# -*- coding: utf-8 -*-
import sys

a = int(sys.stdin.readline())
nums = list(map(int, sys.stdin.readline().split()))
min_num = min(nums)

ans = []
for i in range(1, int(min_num ** (1/2))+1):
    if min_num%i == 0:
        ans.append(i)
        if i**2 != min_num:
            ans.append(min_num//i)
ans.sort(reverse=True)
def run():
    for i in ans:
        ch = True
        for value in nums:
            if value%i != 0:
                ch = False
                break
        if ch:
            print(i)
            return
run()