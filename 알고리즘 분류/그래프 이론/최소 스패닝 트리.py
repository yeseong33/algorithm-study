import sys
from collections import deque
sys.setrecursionlimit(10**6)
INF = int(10e9)

n, m = map(int, sys.stdin.readline().split())

graph = [[] for i in range(n+1)]
indegree = [0] * (n+1)
graph = []

for i in range(m):
    k = list(map(int, sys.stdin.readline().split()))
    graph.append(k)

graph.sort(key= lambda x: x[2])
cicle = [i for i in range(n+1)]
total = 0
count = 0

def find_parent(parent, x):
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])
    return parent[x]

for i in range(m):
    a, b, c = graph[i]
    if find_parent(cicle, a) == find_parent(cicle, b):
        continue
    a = find_parent(cicle, a)
    b = find_parent(cicle, b)
    
    if a > b:
        cicle[a] = b
    else:
        cicle[b] = b
        
        
    total += c

print(total)
    
    