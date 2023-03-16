import sys

n, m = map(int, sys.stdin.readline().split())

dp = [[0] * (m+1)]

for i in range(n):
	k = [0]+list(map(int,sys.stdin.readline().strip()))
	dp.append(k)


ans = 0


for i in range(1, n+1):
    for j in range(1, m+1):
        if dp[i][j] and dp[i-1][j-1]:
            if dp[i][j-1] and dp[i-1][j]:

                if dp[i][j-1] == dp[i-1][j] == dp[i-1][j-1] or min(dp[i][j-1], dp[i-1][j]) + 1 <= max(dp[i][j-1], dp[i-1][j]) or max(dp[i][j-1], dp[i-1][j]) == 1 : 
                    dp[i][j] = min(dp[i][j-1], dp[i-1][j]) + 1
                else:
                    dp[i][j] = max(dp[i][j-1], dp[i-1][j])
                    
                if dp[i][j] > ans:
                    ans = dp[i][j]
        elif dp[i][j]:
            if dp[i][j] > ans:
                ans = dp[i][j]


if n == 1 and m == 1:
    print(dp[1][1])
else:
    print(ans**2)