import sys
from collections import deque
n, m, v = map(int, sys.stdin.readline().split())

graph = dict()
visited = []

for i in range(m):
    a, b = map(int, sys.stdin.readline().split()) 
    if a not in graph:
        graph[a] = [b]
    elif b not in graph[a]:
        graph[a].append(b)
        graph[a].sort()
    
    if b not in graph:
        graph[b] = [a]
    elif a not in graph[b]:
        graph[b].append(a)
        graph[b].sort()
        

graph_2 = graph.copy()

# 스택을 이용한 풀이
def dfsStack(graph, start):
    visited_s, need_visited = list(), list()
    
    need_visited.append(start)
    
    while need_visited:
        
        node = need_visited.pop()
    
        if node not in visited_s:
            visited_s.append(node)
            if node in graph.keys():
                graph[node].sort(reverse = True)
                need_visited.extend(graph[node])
            
    return visited_s



# 재귀를 이용한 풀이
def dfs(graph, start):
    visited.append(start)

    if start in graph.keys():
        for node in graph[start]:
            if node not in visited:
                dfs(graph, node)

dfs(graph, v)

for i in visited:
    print(i, end = ' ')

print()


def bfs(graph, start):
    
    visited = []
    
    queue = deque([start])
    
    while queue:
        node = queue.popleft()
        
        if node not in visited:
            print(node, end = " ")
            visited.append(node)
            if node in graph.keys():
                for i in graph[node]:
                    if i not in visited:
                        queue.append(i)

bfs(graph_2, v)


