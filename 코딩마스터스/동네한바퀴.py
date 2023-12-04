# -*- coding: utf-8 -*-
import sys, heapq

input = sys.stdin.readline
n, m = map(int, input().split())

graph = [[] for i in range(n+1)]

for i in range(m):
    a, b =  map(int, input().split())
    graph[a].append(b)

def bfs():
    q = []
    heapq.heappush(q, -1)
    s = False
    
    while q:
        now = heapq.heappop(q)
        if now == 1:
            print('YES')
            return
        if now == -1:
            now = 1
        for i in graph[now]:
            heapq.heappush(q, i)
    print('NO')
    return

bfs()