import sys

t = int(input())
memo = [[1, 0], [0, 1]]+[[0, 0] for _ in range(40)]


def fibo(n):
    global memo
    if n == 0 or n == 1:
        return
    for i in range(2, n+1):
        memo[i] = [memo[i-1][0] + memo[i-2][0], memo[i-1][1] + memo[i-2][1]]
    

fibo(41)

for i in range(t):
    n = int(sys.stdin.readline())
    print(*memo[n])

