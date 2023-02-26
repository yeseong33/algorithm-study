# import sys


# t = int(input())

# def is_promising(g1, g2):
    
#     for i in g1:
#         k = graph[i]
#         for j in g1:
#             if j in k:
#                 return False
    
#     for i in g2:
#         k = graph[i]
#         for j in g2:
#             if j in k:
#                 return False
    
#     return True

# def dfs(g1, g2):
    
#     if is_promising(g1, g2):
#         return True
    
#     for i in g1:
#         if not visited[i]:
#             visited[i] = 1
#             n_g1 = g1.copy()
#             n_g2 = g2.copy()
            
#             k = graph[i]
            
#             tmp = set()
                        
#             for j in k:
#                 if j in n_g1:
#                     n_g1.remove(j)
#                     tmp.add(j)
            
#             for j in tmp:
#                 n_g2.add(j)
            
#             if dfs(n_g1, n_g2):
#                 return True
    
    
#     return False
    

# for _ in range(2):
#     v, e = map(int, sys.stdin.readline().split())
#     graph = [0]+[[] for i in range(v)]

#     for i in range(e):
#         a,b = map(int, sys.stdin.readline().split())
#         graph[a].append(b)
#         graph[b].append(a)

#     vs = [i for i in range(1, v+1)]

#     g1 = []
#     g2 = []

#     g1.append(1)
#     for i in vs[1:]:
#         if i not in graph[1]:
#             g1.append(i)
#         else:
#             g2.append(i)
            
#     visited = [0] * (v+1)

#     g1 = set(g1)
#     g2 = set(g2)

#     if dfs(g1, g2):
#         print('YES')
#     else:
#         print('NO')
    
                       
                       
## 시간초과로 g1, g2를 리스트의 인덱스를 사용하는 방식으로 바꿈 
                    
import sys
sys.setrecursionlimit(10 ** 6)

t = int(input())

def is_promising(g):
    g1_list = []
    g2_list = []

    for i in range(1, v+1):
        if g[i]:
            g1_list.append(i)
        else:
            g2_list.append(i)
            
    for i in g1_list:
        k = graph[i]
        for j in g1_list:
            if j in k:
                return False
 
    for i in g2_list:
        k = graph[i]
        for j in g2_list:
            if j in k:
                return False
    
    return True


def d(g):
    
    if is_promising(g):
        return True
    
    for i in range(2, v+1):
        if not g[i]:
            # visited[i] = 1

            k = graph[i]
            for j in k:
                g[j] = 1
            if is_promising(g):
                return True
            for j in k:
                g[j] = 0
    
    return False

for _ in range(t):
    v, e = map(int, sys.stdin.readline().split())
    graph = [0]+[[] for i in range(v)]

    for i in range(e):
        a,b = map(int, sys.stdin.readline().split())
        graph[a].append(b)
        graph[b].append(a)

    g = [0] * (v+1)

    
    for i in range(2, v+1):
        if i in graph[1]:
            g[i] = 1
            
    # visited = [0] * (v+1)
    # visited[1] =1 
    
    a = False

    if d(g):
        print('YES')
    else:
        print('NO')


                    
# 1
# 4 3
# 1 4
# 4 3
# 3 2 