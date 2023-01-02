import sys
n, k = map(int, sys.stdin.readline().split())

bag = [list(map(int, sys.stdin.readline().split())) for i in range(n)]
bag.sort()

value = 0

