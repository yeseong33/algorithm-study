def solution(alp, cop, problems):
    problems.sort()
    INF = int(10e9)
    a = 0
    b = 0
    for i in problems:
        a = max(i[0], a)
        b = max(i[1], b)
    dp = [[INF] * (b+1) for _ in range(a+1)]
    dp[alp][cop] = 0
    for i in range(a+1):
        for j in range(b+1):
            if i < a:
                dp[i+1][j] = min(dp[i+1][j], dp[i][j]+1)
            if j < b:
                dp[i][j+1] = min(dp[i][j+1], dp[i][j]+1)
            for alp, cop, alup, coup, cost in problems:
                if i >= alp and j >= cop:
                    a1 = i+alup
                    b1 = j+coup
                    if i+alup >= a: a1 = a
                    if j+coup >= b: b1 = b
                    dp[a1][b1] = min(dp[a1][b1] , dp[i][j] + cost)
                
    print(dp[a][b])
            

    
    answer = 0
    return answer

solution(0, 0, [[0,0,2,1,2],[4,5,3,1,2],[4,11,4,0,2],[10,4,0,4,2]])