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

## ��Ʈ��ŷ ó�� ������� �Լ��� �ҷ����� ��쿡��
# ������ �̸� ������ �ִ��� ��͸� ������� �ʴ� 
# �������� ������ �����ϴ� ���� ����.