import sys

def so(n):
    a2 = 2 
    a5 = 5
    a2_ans = 0 
    a5_ans = 0 
    while True:
        if a2 <= n:
            a2_ans += n // a2
            a2 *= 2
        else:
            break
    
    while True:
        if a5 <= n:
            a5_ans += n // a5
            a5 *= 5
        else:
            break
    return [a2_ans, a5_ans]
    


n, k = map(int, sys.stdin.readline().split())


p1 = so(n)
p2 = so(k)
p3 = so(n-k)

x2 = p1[0] - p2[0] -p3[0]
x5 = p1[1] - p2[1] -p3[1]
ans = min(x2, x5)
print(ans)


# 팩토리얼을 소인수분해 하여 0이 나올 수 있는 경우의
# 수를 구한다 생각