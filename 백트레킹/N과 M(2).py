import sys

n, m = map(int, sys.stdin.readline().split())
l =[]
r = []

def loop():
    if len(l) == m:
        k = l.copy()
        k.sort()
        if k not in r:
            print(' '.join(map(str, l)))
            r.append(k)
        return
    else:
        for i in range(1, n+1):
            if i not in l:
                l.append(i)
                loop()
                l.pop()


# 4 2 
# 1 2 3 4
# 1 1 x
# 1 2
# 1 3
# 1 4
# 2 1 x
# 2 2 x
# 2 3 
# 2 4 
# 3 1 x
# 3 2 x
# 3 3 x
# 3 4 

