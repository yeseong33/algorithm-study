import sys 

n = int(input())

idx = {0:[1, 2], 1:[0, 2], 2:[0, 1]}
k = [0, 0, 0]

for i in range(n):
    cost = list(map(int, sys.stdin.readline().split()))
    
    for j in range(3):
        cost[j] += min(k[idx[j][0]], k[idx[j][1]])
    k = cost

print(min(cost))
