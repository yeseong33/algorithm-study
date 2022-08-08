import sys
n = int(input())
scores = list(map(int, sys.stdin.readline().split(' ')))
m = max(scores)
for i in range(len(scores)):
    scores[i] = scores[i]/m * 100
avg = sum(scores)/n
print(avg)