import sys
sys.setrecursionlimit(10 **6)


n = int(input())

nodes = list(map(int, sys.stdin.readline().split()))

graph = [[] for i in range(n)]

startNode = 0

for i in range(n):
    p = nodes[i]
    
    # 최상위 부모일 때
    if p == -1:
        startNode = i
        continue
    
    # 부모 노드에 노드 할당
    graph[p].append(i)
    
ignore = int(input())

visited = [0] * n
visited[ignore] = 1 
leaf = 0 

def dfs(n):
    global leaf
    
    visited[n] = 1
     
    check = False
    
    for i in graph[n]:
        if not visited[i]:

            check = True
            dfs(i)
            
    if not check:
        leaf += 1       


if startNode == ignore:
    print(leaf)
else: 
    dfs(startNode)
    print(leaf)
