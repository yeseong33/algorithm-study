import sys

n, m = map(int, sys.stdin.readline().split())

c = [[0] * (n+1)]

chicken = []
house = []
ans = 10000000000


for i in range(n):
    k = list(map(int, sys.stdin.readline().split()))
    c.append([0] + k)
    
    
for i in range(1, n+1):
    for j in range(1, n+1):
        what = c[i][j]
        if what == 1:
            house.append((i, j))
        elif what == 2:
            chicken.append((i, j))
            
            
def distance(a, b):
    x1 = a[0]
    y1 = a[1]
    x2 = b[0]
    y2 = b[1]
    return abs(x1-x2) + abs(y1-y2)


def dfs(best, idx):
    global ans
    
    if len(best) == m:
        total = 0
        for i in house:
            distance_of_house = 2 * n
            for j in best:
                d = distance(i, j)
                if distance_of_house >= d:
                    distance_of_house = d
            total += distance_of_house
        if total <= ans:
            ans = total
    else:
        for i in range(idx, len(chicken)):
            best.append(chicken[i])
            dfs(best, i+1)
            best.pop()
            

dfs([], 0)
print(ans)