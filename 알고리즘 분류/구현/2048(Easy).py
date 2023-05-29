# 1. 될 수 있는 최대 값을 구함 - 모든 값을 더한 값
# 위 값보다 같거나 크면 - 최적인 경우
# 2. 5번의 경우의 수 - 1024의 경우의 수를 모두 살펴봐야 함
# dfs로 들어가면서 최적인 경우에 나올 수 있도록 짬

# 움직이는 함수

import sys

n = int(input())

# borad = [[0] * n for _ in range(n)]
borad_origin = []

for i in range(n):
    k = list(map(int, sys.stdin.readline().split()))
    borad_origin.append(k)
    
# 가장 큰 값
max_size = 0
for i in range(n):
    for j in range(n):
        if max_size < borad_origin[i][j]:
            max_size = borad_origin[i][j]


# 움직이고 확인하는 함수
# borad와 방향을 변수로 받음
def move(borad, way):
    global max_size
    new_borad = [[0] * n for _ in range(n)]
    
    if way == 0:
        for i in range(n):
            m = 0
            p = 0
            
            for j in range(n):
                if borad[i][j] == 0:
                    continue
                if p == 0:
                    new_borad[i][m] = borad[i][j]
                    p += 1

                elif p == 1: 
                    if borad[i][j] == new_borad[i][m]:
                        new_borad[i][m] += borad[i][j]
                        if new_borad[i][m] > max_size:
                            max_size = new_borad[i][m]
                        m += 1
                        p = 0
                        
                    else:
                        m += 1
                        new_borad[i][m] += borad[i][j]
                        
        
        return new_borad
    elif way == 1:
        for i in range(n):
            arr = [0] * n
            m = n-1
            p = 0
            
            for j in range(n-1, -1, -1):
                if borad[i][j] == 0:
                    continue
                if p == 0:
                    new_borad[i][m] += borad[i][j]
                    p += 1

                elif p == 1: 
                    if borad[i][j] == new_borad[i][m]:
                        new_borad[i][m] += borad[i][j]
                        if new_borad[i][m] > max_size:
                            max_size = new_borad[i][m]
                        m -= 1
                        p = 0
                        
                    else:
                        m -= 1
                        new_borad[i][m] += borad[i][j]
        return new_borad
    elif way == 2:
        for i in range(n):
            m = 0
            p = 0
            
            for j in range(n):
                if borad[j][i] == 0:
                    continue
                if p == 0:
                    new_borad[m][i] += borad[j][i]
                    p += 1

                elif p == 1: 
                    if borad[j][i] == new_borad[m][i]:
                        new_borad[m][i] += borad[j][i]
                        if new_borad[m][i] > max_size:
                            max_size = new_borad[m][i]
                        m += 1
                        p = 0
                        
                    else:
                        m += 1
                        new_borad[m][i] += borad[j][i]
                    
        return new_borad
    
    elif way == 3:
        for i in range(n):
            m = n-1
            p = 0
            
            for j in range(n-1, -1, -1):
                if borad[j][i] == 0:
                    continue
                if p == 0:
                    new_borad[m][i] += borad[j][i]
                    p += 1

                elif p == 1: 
                    if borad[j][i] == new_borad[m][i]:
                        new_borad[m][i] += borad[j][i]
                        if new_borad[m][i] > max_size:
                            max_size = new_borad[m][i]
                        m -= 1
                        p = 0
                        
                    else:
                        m -= 1
                        new_borad[m][i] += borad[j][i]
                    
        return new_borad
        

# dfs로 모든 경우를 찾아 가장 큰 값을 찾음
def dfs(borad, count):
    # 5번 찾았을 경우는 retrun
    if count == 5:
        return
    
    # 4방향으로 dfs 적용
    for i in range(4):
        # 움직임 (상하좌우) 
        tmp = move(borad, i)
        # 움직여 만들어진 tmp를 넘김
        dfs(tmp, count+1)
            
        
# 3
# 2 4 2
# 4 4 4
# 8 8 8

# 5
# 2 4 2 4 4
# 2 2 2 2 2 
# 2 1 1 2 1 
# 2 4 4 4 2
# 4 2 2 4 2

dfs(borad_origin, 0)
print(max_size)