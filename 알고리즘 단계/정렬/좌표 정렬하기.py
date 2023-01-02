import sys


n = int(sys.stdin.readline())

nums = [list(map(int,sys.stdin.readline().split())) for i in range(n)]

nums.sort()


for i in range(n):
    print(nums[i][0], nums[i][1])



####
from sys import stdin, stdout

dot = stdin.readlines()[1:]

dot.sort(key=lambda x: (int(x.split()[0]), int(x.split()[1])))

stdout.write(''.join(dot))


    