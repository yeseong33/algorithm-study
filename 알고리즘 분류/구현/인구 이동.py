import sys
from collections import deque

n, r, l = map(int, sys.stdin.readline().split())

A = []

for i in range(n):
    k = list(map(int, sys.stdin.readline().split()))
    A.append(k)
    
d = [(0, 1), (1, 0), (0, -1), (-1, 0)]

def move():
    count = 0
    
    while True:
        g = 1
        q = deque()
        
        visited = [[0] * n for _ in range(n)] 
        A_G = [[0] * n for _ in range(n)] 
        
        for i in range(n):
            for j in range(n):
                
                if not visited[i][j]:
                    q.append((i, j))
                    visited[i][j] = 1 
                    A_G[i][j] = g
                    g += 1
                    
                
                while q:
                    
                    x, y = q.popleft()
                    pre_p = A[x][y]
                    pre_g = A_G[x][y]
                    
                    for k in range(4):
                        new_x, new_y = x + d[k][0], y+d[k][1]
                        
                        if 0 <= new_x < n and 0 <= new_y < n:
                            if not visited[new_x][new_y]:
                                at_p = A[new_x][new_y]
                                diff = abs(pre_p-at_p)
                                
                                if r <= diff <= l:
                                    A_G[new_x][new_y] = pre_g
                                    visited[new_x][new_y] = 1
                                    q.append((new_x, new_y))
        
        # print("A_g-f")
        # for i in A_G:
        #     print(*i)
        
        # print("A_g-ww")
        # for yry in A_G:
        #     print(*yry)
            
        group = [0] * (n**2 + 1) 
        # print(group)
        group_p = [0] * (n**2 + 1) 
        for i in range(n):
            for j in range(n):
                # print(i, j)
                # print(A_G[i][j])
                # if A_G[i][j] == 13:
                #     print('fef')
                    
                group[A_G[i][j]] += 1
                group_p[A_G[i][j]] += A[i][j]
        
        # print(group)
        # print(group_p)
        result = [0] * (n ** 2 + 1) 
        for i in range(1, n**2+1):
            
            if group[i] != 0: 
                result[i] = group_p[i]//group[i]
        
        for i in range(n):
            for j in range(n):
                A[i][j] = result[A_G[i][j]]

        # print("A")
        # for oo in A: 
        #     print(*oo)
        # print("A_g")
        # for i in A_G:
        #     print(*i)
        # print(g)
        if g == n ** 2+1:
            return count 
        else:
            count += 1
            

print(move())

# 2 1 66
# 1 0
# 0 100
#  1 9 