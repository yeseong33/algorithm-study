import sys

n, k = map(int, sys.stdin.readline().split())

coins = [int(sys.stdin.readline()) for i in range(n)]
coins.sort(reverse=True)
count = 0

for i in coins:
    if k // i != 0:
        t = k // i
        count += t
        k -= t * i 

    if k == 0:
        break

print(count)
