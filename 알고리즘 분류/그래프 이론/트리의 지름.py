## dfs로 풀려고 했으나, 약간 bfs 방식이 섞인것 같음
import sys
sys.setrecursionlimit(10**5)

v = int(input())

graph = [[] for i in range(v+1)]


for i in range(v):
    k = list(map(int, sys.stdin.readline().split()))
    node = k[0]
    k = k[1:-1]
    for j in range(0, len(k)//2):
        tm = k[2*j:2*j+2]
        graph[node].append(tm)



def dfs(n, r):
    global max_r, max_node

    visited[n] = 1
    con = False
    
    for i in range(len(graph[n])):
        if not visited[graph[n][i][0]]:
            con =True
            break
    
    if not con:
        if r > max_r:
            max_r = r
            max_node = n
        return
    
    k = len(graph[n])
    
    for i in range(k):
        if not visited[graph[n][i][0]]:
            r += graph[n][i][1]
            dfs(graph[n][i][0], r)
            r -= graph[n][i][1]



max_r = 0
max_node = 0 
visited = [0] * (v+1)
dfs(1, 0)
visited = [0] * (v+1)
dfs(max_node, 0)
print(max_r)