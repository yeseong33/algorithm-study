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

loop()
print(r)
