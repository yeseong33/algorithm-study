import sys 

n, m = map(int, sys.stdin.readline().split())
l = []



def dfs():
    if len(l) == m:
        print(' '.join(map(str, l)))
        return
    else:
        for i in range(1, n+1):
            # if i not in l:
                l.append(i)
                dfs()
                l.pop()

dfs()