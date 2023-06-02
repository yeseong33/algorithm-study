# n개의 원소를 담은 리스트를 만듦 
# 각 인덱스는 그 건물을 짓는데 걸리는 시간
# 관계를 체크해서 그 인덱스가 0이 되는 시간을 구함
# dp + dfs


import sys
from collections import deque

# 몇개의 건물인지 
n = int(input())

# 건물 번호를 기준으로 graph를 만듦 - 위상정렬에 사용
grah = [[] for i in range(n+1)]
# 건물을 짓는데 걸리는 시간
time = [0] * (n+1)
# 건물에 할당된 진입 차수
indegree = [0] * (n+1)

# 적절하게 분배
for i in range(1, n+1):
    k = list(map(int, sys.stdin.readline().split()))
    time[i] += k[0]
    for j in k[1:-1]:
        grah[j].append(i)
        
        indegree[i] += 1

# 위상정렬 + dp
def topology_sort():
    # 현재 건물을 짓는데 걸리는 최소 시간을 구하기 위함
    result = [0] *(n+1)
    # 위상정렬을 구현하기 위한 q 
    q = deque()
    
    # 진입 차수가 0인 값들을 q에 넣어줌
    for i in range(1, n+1):
        if indegree[i] == 0:
            q.append(i)
            
    # 초기 건물 짓는 시간을 본 건물 짓는 시간만으로 한정
    result = time[:]

    # q가 빌때 까지 - 모든 노드를 방문 했을 때 까지
    while q: 
        # 현재 건물
        now = q.popleft()

        # 현재 건물이 지어지고 나서 지을 수 있는 건물들에 대해 조사
        for k in grah[now]:
            # 진입 차수를 하나 줄임
            indegree[k] -= 1
            
            # 진입 차수가 0일 경우 - 더 이상 이 건물을 고려하지 않음
            if indegree[k] == 0:
                # q에 넣어 다음 건물들에 대해 계산할 수 있도록 함
                q.append(k)
            # 진입 차수와 상관 없이 k 건물이 지어지기 위해서는 진입되는 건물들이 지어저야 함
            # 이때 시간이 오래 걸리는 건물이 이어지고 나서 k 건물이 지어질 수 있으므로
            # 현재까지의 건물이 지어지는 시간 값과 k를 짓기 위해 필요한 건물이 지어진 시간값 + k 건물 지어지는 시간
            # 중 더 큰 값을 k 건물이 지어지는 시간으로 설정
            result[k] = max(result[now]+time[k], result[k])
    # 결과 값을 반환
    return result
    
# 결과값을 받음
ans = topology_sort()

# 건물 번호 순서대로 출력
for i in ans[1:]:
    print(i) 



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