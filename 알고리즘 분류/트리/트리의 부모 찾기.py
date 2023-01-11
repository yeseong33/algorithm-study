## visited 에 직접 값을 넣는 것이 아니라
## n+1 list를 만들어 false, true에 대한 정보를 넣어 속도를 올렸다.

# BFS 방법
import sys
from collections import deque

n = int(input())

ans = [0 for i in range(n+1)]
ans_2 = ans.copy()
ans_3 = ans.copy()
tree = {}

for i in range(n-1):
    a, b = map(int, sys.stdin.readline().split())
    if a not in tree:
        tree[a] = [b]
    elif b not in tree[a]:
        tree[a].append(b)
    
    if b not in tree:
        tree[b] = [a]
    elif a not in tree[b]:
        tree[b].append(a)

def bfs(start): 
    
    visited = [False] * (n+1)
    
    queue = deque([start])
    
    while queue:
        node = queue.popleft()
        if not visited[node]:
            visited[node] = True
            for i in tree[node]:
                if ans[i] == 0: 
                    ans[i] = node
            if node in tree:  
                for i in tree[node]:
                    if not visited[i]:
                        queue.append(i)


bfs(1)

for i in range(2, n+1):
    print(ans[i])

        
        

# DFS 방법 


# 재귀 방식 사용
# n 이 커질경우 RecursionError 를 나타냄

visited_dfs = [False for i in range(n+1)]

def dfs(start):
    if not visited_dfs[start]:
        visited_dfs[start] = True
        
    if start in tree:
        for i in tree[start]:
            if not visited_dfs[i]:
                if ans_2[i] == 0:
                    ans_2[i] = start
                dfs(i)
                
dfs(1)
for i in range(2, n+1):
    print(ans_2[i])
    
    
# 스택을 활용한 풀이
# 재귀 방법과 마찬가지로 RecursionError를 나타냄
def dfsStack(start):
    need_visited = []
    visited_dfsStack = [False]*(n+1)
    need_visited.append(start)
    
    while need_visited:
        node = need_visited.pop()

        if not visited_dfsStack[node]:
            visited_dfsStack[node] = True
        
            if node in tree:
                for i in tree[node]:
                    if ans_3[i] == 0:
                        ans_3[i] = node
                    if i not in need_visited:
                        need_visited.append(i)
dfsStack(1)
for i in range(2, n+1):
    print(ans_3[i])
    
        