import sys

n, k = map(int, sys.stdin.readline().split())

score = list(map(int, sys.stdin.readline().split()))

score.sort()
print(score[-k])