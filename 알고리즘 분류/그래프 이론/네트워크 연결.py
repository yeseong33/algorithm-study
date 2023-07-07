import sys
INF = int(1e10)
n = int(input())

m = int(input())


cost = [[INF] * (n+1) for i in range(n+1)]
parent = [i for i in range(n+1)]

edge = []

for i in range(m):
    a, b, c = map(int, sys.stdin.readline().split())
    edge.append([a, b, c])
        
def find_parent(parent, x):
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])
    return parent[x]

def union_parent(parent, x, y):
    x = find_parent(parent, x)        
    y = find_parent(parent, y)
    
    if x < y:
        parent[y] = x
    else:
        parent[x] = y         

co = 0 

edge.sort(key = lambda x: x[2])
        
for i in edge:
    a, b, c = i[0], i[1], i[2]
    
    if find_parent(parent, a) != find_parent(parent, b):
        union_parent(parent, a, b)
        co += c 
print(co)