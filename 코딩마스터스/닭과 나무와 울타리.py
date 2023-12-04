
          
from sys import stdin
from itertools import combinations
from itertools import product

input = stdin.readline

n = int(input())

pos = [list(map(int, input().split())) for i in range(n)]

ans = [[] for _ in range(n+1)]
ans[0].append(1)

def dis(a, b):
    return (abs(a[0]-b[0]) + abs(a[1]-b[1]))**0.5
def make_combi(arr, idx):
    r = [item for sublist in arr[1:] for item in sublist]
    print(r)
    print(arr)
    combi = list(combinations(r, idx-1))
    print('c', combi)
    for i in range(len(combi)):
        combi[i] = tuple(arr[0])+ combi[i]
    return combi

def make_dis_table(arr, c):
    n = len(arr)
    result = []
    table = [[0] * n for i in range(n)]
    for i in range(n):
        for j in range(n):
            table[i][j] = (dis(arr[i], arr[j]), j)
        table[i].sort()
        print(table[i])
        tmp = []
        visited = []  
        count = c 
        print(table)
        j = 0
        while j < n:
            if count == 0:
                break
            now = table[i][j]
            print(now)
            if now[0] in visited:
                tmp[-1].append(now[1])
                j +=1 
                continue
            tmp.append([now[1]])
            print(tmp)
            visited.append(now[0])
            j += 1
            count -= 1
        print(tmp)
        combi = make_combi(tmp, c)
        print('com', combi)
        for now in combi:
            tmp_2 = []
            for idx in now:
                tmp_2.append(pos[idx])
            result.append(tmp_2)
            
    print('len of result:', len(result))
    print(result)
    return result
    
r = make_dis_table(pos, 3)

def make_small(arr, idx):
    min_cost = 10 ** 12
    for j in arr:
        print('j',j)
        j = list(j)
        j.sort(key = lambda x: x[1])
        y_max = j[-1][1]
        y_min = j[0][1]
        j.sort(key = lambda x: x[0])
        x_max = j[-1][0]
        x_min = j[0][0]
        a = (y_max+1) - (y_min-1) 
        b = (x_max+1) - (x_min-1) 
        k = (a+b) * 2
        min_cost = min(k, min_cost)
    ans[idx].append(min_cost)

def run():

    for j in range(5):
        chiken_tree = n-j
        idxs = make_dis_table(pos, chiken_tree)
        for point in idxs:
            print('개수: ', chiken_tree)
            pack = []
            for jj in combinations(point, chiken_tree):
                pack.append(jj)
            print('pack: ', pack)
            make_small(pack, chiken_tree)
            print('ans', ans)

run()

for i in range(n, n-5, -1):
    print(min(ans[i]))



