import sys

n = int(sys.stdin.readline())

nums = [list(map(int, sys.stdin.readline().split())) for i in range(n)]

nums.sort(key = lambda x: (x[1], x[0]))


for i in range(n):
    print(nums[i][0], nums[i][1])




####
# n = int(sys.stdin.readline())
# def f(s):
#     a,b = map(int,s.split())
#     return a/1000000+b
# a = sorted([sys.stdin.readline() for _ in range(n)],key=f)
# print(a)
# print("".join(a))


## 
# split() �Լ��� ������ �����ϸ�, \n \t�� ���� ��ɵ� ó���� �ش�.
# split(' ')�� ��� ������ ������ ����� ������ �ش�.
