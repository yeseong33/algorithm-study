# -*- coding: utf-8 -*-
import sys
from collections import deque
import heapq
# bfs 최소 도달로 문제 해결
n = int(input())

dist =[]
for i in range(n):
    a, b = map(int, input().split())
    dist.append([a, b])
distance, p = map(int,input().split())

con = [0] * (distance+1) 

for a, b in dist:
    con[a] = b
    
load =[-1] * (distance+1)

c = 0

pc = []
po = p
for i in range(1, distance+1):
    
    if po > 0:
        if con[i]:
            pc.append([i, con[i]])
        load[i] = c
    else:
        if pc != []:
            pc.sort(key = lambda x: (x[1]-(i-x[0])))
            a, b = pc.pop()
            po += b
            c += 1
            load[i] = c 


    po -= 1
    
    if po < 0:
        break
print(load[-1])


