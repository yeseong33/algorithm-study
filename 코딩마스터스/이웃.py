import sys
input = sys.stdin.readline

n, m, k = map(int, input().split())
graph = [[] for _ in range(n+1)]
nodes_value = [0]
nodes = []
for i in range(1, n+1):
    value = int(input())
    nodes.append([value, i])
    nodes_value.append(value)
    
nodes.sort(key = lambda x: -x[0])
nodes_idx = []

for i in nodes:
    nodes_idx.append(i[1])

for i in range(m):
    a, b=  map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)
        
total_count=0
for _ in range(2):
    for i in nodes_idx:
        for j in graph[i]:
            gap = nodes_value[i] - nodes_value[j]
            if gap > k:
                count = gap -k
                nodes_value[j] += count
                total_count += count
print(total_count)
    