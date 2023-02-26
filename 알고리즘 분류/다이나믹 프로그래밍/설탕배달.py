import sys

n = int(input())
memo = [0] * 5001
memo[3] = 1
memo[5] = 1
 
def dp(n):
    
    for i in range(6, n+1):
        if not (memo[i-5] or memo[i-3]) :
            continue
        if not memo[i-3]:
            memo[i] = memo[i-5] +1
        elif not memo[i-5]: 
            memo[i] = memo[i-3] +1
        else: 
            memo[i] = min(memo[i-5], memo[i-3]) + 1
    


dp(n)

if memo[n]:
    print(memo[n])
else:
    print(-1)




















