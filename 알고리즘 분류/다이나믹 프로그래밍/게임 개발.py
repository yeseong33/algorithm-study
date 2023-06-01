# n개의 원소를 담은 리스트를 만듦 
# 각 인덱스는 그 건물을 짓는데 걸리는 시간
# 관계를 체크해서 그 인덱스가 0이 되는 시간을 구함
# dp + dfs


import sys
from collections import deque

n = int(input())

grah = [[] for i in range(n+1)]
time = [0] * (n+1)
indegree = [0] * (n+1)

for i in range(1, n+1):
    k = list(map(int, sys.stdin.readline().split()))
    time[i] += k[0]
    for j in k[1:-1]:
        grah[j].append(i)
        
        indegree[i] += 1


# for i in grah:
#     print (i)

# print(indegree)

def topology_sort():
    result = [0] *(n+1)
    q = deque()
    
    for i in range(1, n+1):
        if indegree[i] == 0:
            q.append(i)
    for i in range(1 , n+1):
        result[i] = time[i]
            
    while q: 
        now = q.popleft()

        for k in grah[now]:
            indegree[k] -= 1
            
            if indegree[k] == 0:
                q.append(k)
            
            result[k] = max(result[now]+time[k], result[k])
        

    return result
    
ans = topology_sort()

for i in ans[1:]:
    print(i) 

        # 
# 5
# 10 -1
# 10 1 -1
# 4 1 -1
# 4 3 1 -1
# 3 3 -1


# dp(1, 1)
# dp(2, 2)
# dp(3, 3)
# dp(4, 4)
# dp(5, 5)


# print(visited)