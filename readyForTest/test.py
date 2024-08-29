import sys

def makeSettings():
    n, q = map(int, sys.stdin.readline().split())
    graph = [[] for i in range(n+1)]
    makeTree(n, graph)
    return graph, q

def makeTree(n, graph):
    for i in range(n-1):
        a, b, usado = map(int, sys.stdin.readline().split())
        graph[a].append((b, usado))
        graph[b].append((a, usado))

def answer(graph, q):
    answers = []
    for i in range(q):
        k, v = map(int, sys.stdin.readline().split())
        count = 0
        q = [(v, int(10e9))]
        visited = set()
        visited.add(v)
        while q:
            now, d = q.pop()
            if d < k: continue
            for target, usado in graph[now]:
                if target in visited: continue
                visited.add(target)
                if d < usado:
                    usado = d
                if usado >= k:
                    count += 1
                q.append((target, usado))
        answers.append(count)
    for i in answers:
        print(i)
def solve():
    graph, q = makeSettings()
    answer(graph, q)
    

solve()

