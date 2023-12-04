import sys
input = sys.stdin.readline
print = sys.stdout.write

n = int(input())

def bfs(n):
    num = [(n, 0)]
    
    while num:
        now, count = num.pop()
        if now == 1:
            print(str(count))
            return 
        a = []
        if now%2==0:
            a.append(now//2)
        if now%3==0:
            a.append(now//3*2)
        if now%5==0:
            a.append(now//5*4)
        for i in a:
            num.append((i, count+1))
    
    print('-1')

bfs(n)
