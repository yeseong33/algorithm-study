# 값을 더해나감
import sys, heapq

n = int(input())
cards = []

for i in range(n):
    k = int(sys.stdin.readline().strip())
    heapq.heappush(cards, k)

   
ans = 0

if n == 1:
    print(0)
else:
    while len(cards) != 1:
        a = heapq.heappop(cards)
        b = heapq.heappop(cards)
        result = a + b
        ans += result
        heapq.heappush(cards, result)
    print(ans)
        





