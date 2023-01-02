import sys

t = int(sys.stdin.readline())

for i in range(t):
    n = int(sys.stdin.readline())
    clothes = dict()


    for j in range(n):
        a, c = map(str, sys.stdin.readline().split())
        if c not in clothes:
            clothes[c] = 1
        else:
            clothes[c] += 1


 
    ans = 1
    for k in clothes.values():
        ans *=  (k+1)
    
    print(ans-1)