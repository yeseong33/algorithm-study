n = int(input())

while True:
    for i in range(2, n+1):
        if n % i == 0:
            k = i
            break
    if n == 1:
        break
    else:
        n = n // k
        print(k)
        
        
##
n = int(input())
k = 2

# n ���� 1�� �Ǹ� ����
while n != 1:
    ## �Ҽ��������� Ȯ��
    if k > n **(0.5):
        print(n)
        exit(0)
        
    # ���μ� ���� ������ �� �� ��� ���μ� ������
    # �ƴҰ�� k ���� 1�� ������Ŵ -> ��� ���� ��ħ
    if n % k == 0:
        print(k)
        n //= k
    else:
        k += 1
        