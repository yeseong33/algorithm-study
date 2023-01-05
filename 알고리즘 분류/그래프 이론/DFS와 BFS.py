import sys

n, m, v = map(int, sys.stdin.readline().split())

graph = dict()
visited = []

for i in range(m):
    a, b = map(int, sys.stdin.readline().split()) 
    if a not in graph.keys():
        graph[a] = [b]
    else:
        graph[a] = graph[a] + [b]

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

dfs(graph, 1)
print(visited)

print(dfsStack(graph, 1))
