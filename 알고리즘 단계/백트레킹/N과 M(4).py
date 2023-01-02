import sys

n, m = map(int, sys.stdin.readline().split())

l = []
ans = []

def d():
    if len(l) == m:
        print(' '.join(map(str, l)))            
        return 
    else:
        for i in range(1, n+1):
            if l == [] or i >= l[-1]:
                l.append(i)
                d()
                l.pop()

d()

## 백트레킹 처럼 재귀적을 함수를 불러오는 경우에는
# 조건을 미리 설정해 최대한 재귀를 사용하지 않는 
# 방향으로 조건을 설정하는 것이 좋다.