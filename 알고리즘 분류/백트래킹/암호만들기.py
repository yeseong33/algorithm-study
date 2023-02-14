import sys

l, c= map(int, sys.stdin.readline().split())

alpha = list(map(str, sys.stdin.readline().split()))
alpha.sort()


m = set({'a', 'e', 'i', 'o', 'u'})

def dfs(password, idx):
    
    if len(password) == l:
        count = 0
        for i in password:
            if i in m:
                count += 1
        
        if count >= 1 and abs(count-len(password)) >= 2:
            print(*password, sep='')
    else:
        for i in range(idx, c):
            password.append(alpha[i])
            dfs(password, i+1)
            password.pop()
dfs([], 0)

            
        
