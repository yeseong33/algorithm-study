# -*- coding: utf-8 -*-
import sys

n, m = map(int,sys.stdin.readline().split())
parent = [i for i in range(n+1)]

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

for i in range(m):
    a, b = map(int,sys.stdin.readline().split())
    union_parent(parent, a, b)
    
count = [0] * (n+1)
for i in range(1, n+1):
    count[parent[i]] += 1
print(count.index(max(count)))



