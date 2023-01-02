import sys
n, m = map(int, sys.stdin.readline().split())
temp = [[0] * (n+1)]
dp = [[0] * (n+1)]

for i in range(n):
    k = [0]+list(map(int, sys.stdin.readline().split()))
    temp.append(k)
    dp.append([0]*(n+1))

for i in range(n):
    for j in range(n):
        dp[i+1][j+1] = temp[i+1][j+1]+ dp[i+1][j] + dp[i][j+1] - dp[i][j]
print(dp)
print(temp)
[[0, 0, 0, 0, 0], 
 [0, 1, 2, 3, 4], 
 [0, 2, 3, 4, 5], 
 [0, 3, 4, 5, 6], 
 [0, 4, 5, 6, 7]]
for _ in range(m):  
    x1, y1, x2, y2 = map(int, sys.stdin.readline().split())
    
    total = dp[x2][y2] - dp[x2][y1-1] - dp[x1-1][y2] + dp[x1-1][y1-1] 
    print(total)

# k = [1,2,3]
# k[1] = 4
# print(k)