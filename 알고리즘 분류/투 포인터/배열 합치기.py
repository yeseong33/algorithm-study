import sys
# 가장 큰 수를 표현하기 위한 10억
INF = int(1e9)
 
# 값을 받음
n, m  = map(int, sys.stdin.readline().split())
a = list(map(int, sys.stdin.readline().split()))
b = list(map(int, sys.stdin.readline().split()))

# 시작 인덱스
p1 = 0
p2 = 0

# 리스트를 다 사용하기 위한 마지막 인덱스
a += [INF]
b += [INF]

# 두 리스트를 크기를 정렬해주며 합치는 함수
def list_hap(p1, p2):
    # 합쳐지는 리스트
    r = []
    
    # 두 인덱스 값이 모두 마지막 인덱스를 가리킬 때 까지 
    # while 문을 돌림
    while p1 != n or p2 != m:
        # 어떤 수가 더 작은지 확인
        # 이때 가장 마지막 값은 INF 이므로 그전 값까지 표시 됨
        head = min(a[p1], b[p2])
        # 더 작은 값 리스트에 추가
        r.append(head)
        
        # 값이 사용되면 다음 인덱스를 가리킴
        if head == a[p1]:
            p1 += 1
        else: 
            p2 += 1
    return r
    

r = list_hap(0, 0)

print(*r)

    
    

