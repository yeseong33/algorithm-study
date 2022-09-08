## https://www.acmicpc.net/board/view/50440
import sys

n = int(input())
nums = [list(map(int, sys.stdin.readline().split())) for i in range(n)]

check = [False] * n
check[0] = True
Min = 99 * (n//2) * (n-1)


[True, True, False, False]


def team(d, e):
    global Min
    if d == n//2:
        a = []
        b = []
        # ���� ������ ��� 
        for j in range(n):
            if check[j]:
                a.append(j)
            else:
                b.append(j)
            
        
        # ������ ������ ���
        ats = 0
        for i, a1 in enumerate(a):
            for a2 in a[i+1:]:
                ats += nums[a1][a2] + nums[a2][a1]
                
        bts = 0
        for i, b1 in enumerate(b):
            for b2 in b[i+1:]:
                bts += nums[b1][b2] + nums[b2][b1]
                
        # for i in range(n):
        #     for j in range(i+1, n):
        #         ~~
        
        
        # �ּ����� �Ǻ�
        k  = abs(ats-bts)
        if Min > k:
            Min = k
        return
                
            # [True, False, False, False]
    else:
        for i in range(e, n):
                check[i] = True
                team(d+1, i+1)
                check[i] = False    
                

team(1, 1)
print(Min)


## �ð����⵵ ������ ���鼭 ���߿� �ٽ� Ǯ��
## enumerate() �Լ� ����� �˾� �α�