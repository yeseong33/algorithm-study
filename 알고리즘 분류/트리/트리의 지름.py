# import sys
# n = int(input())

# ends = []
# graph = [[] for i in range(n+1)]
# lenths = [[0]*(n+1) for _ in range(n+1)]
# for_ends = [[] for i in range(n+1)]


# for i in range(1, n):
#     a, b, c = map(int, sys.stdin.readline().split())
#     for_ends[a].append([b, c])
#     graph[a].append(b)
#     lenths[a][b] += c
#     graph[b].append(a)
#     lenths[b][a] += c    

# for i in range(1, n+1):
#     if for_ends[i] == []:
#         ends.append(i)
            

# # def dfs(start):
# #     global total, visited
# #     node = graph[start]
# #     visited[start] = 1
    
    
# #     for next_node in node:
# #         if visited[0] == 0:
# #             next = next_node[0]
# #             total += next_node[1]
# #             dfs(next)
# #             total -= next_node[1]
            
# #     if start in ends:
# #         ans.append(total)




# def dfs_stack(start, visited, graph):
    
#     need_visited = [start]
    
#     while need_visited:
        
#         node = need_visited.pop()
#         if visited[node] != 0:
#             visited[node] = 1
            
#             for i in graph[node]:
#                 if visited[i] != 0:
#                     visited[node] = visited[i] + lenths[i][node]
#                     need_visited.append(i)
        

#     print(visited)



# visited =[]
# result = []
# record = [0 for i in range(n+2)]


# for i in ends:
#     ans = [0 for _ in range(n+1)]
#     record.append(i)    
#     visited = record[:]
#     dfs_stack(i, visited, graph)
# # print(max(result))


import sys

n = int(input())
graph = [[] for _ in range(n+1)]

for _ in range(n-1):
    a, b, c = map(int, sys.stdin.readline().split())
    graph[a].append([b, c])
    graph[b].append([a, c])

visited = [-1 for i in range(n+1)]

def dfs(start):
    
    visited[start] = 0
    need_visited = [start]
    
    while need_visited:
        node = need_visited.pop()
        
        for k in graph[node]:
            a, b = k
            if visited[a] == -1:
                visited[a] = visited[node] + b
                need_visited.append(a)          

        
dfs(1)
node = visited.index(max(visited))
visited = [-1 for i in range(n+1)]

dfs(node)
print(max(visited))

# 길이가 최대가 되는 것이 핵심
# 이를 잘 이용해야 함
# 메모리 초과가 안나게 구조를 명확히 짜야 함

# 재귀 사용시(최대 깊이 설정, defult = 1000)
# import sys
# sys.setrecursionlimit(10 ** 6)
# 코드를 사용

# sys.setrecursionlimit은 "주어진 깊이만큼의 재귀를 충분히 수행할 수 있는" 크기의 메모리를 미리 할당받는 역할을 합니다. 
# 여유 있게 잡기 때문에 100만 번의 재귀를 허용하기 위해서 받는 메모리의 양은 어마어마하고, 그 즉시 문제에 주어진 메모리 
# 제한을 초과하게 됩니다. 이 문제에서는 n이 1만 이하라 100만까지 필요하지 않습니다. 그냥 10**4만큼만 잡아주면 됩니다.