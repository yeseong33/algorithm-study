import sys

def EA(a, b):
    
    if a % b != 0:
        return EA(b, a%b)
    else:
        return b

n = int(sys.stdin.readline())


for i in range(n):
    a, b = map(int, sys.stdin.readline().split())
    if a < b:
        a, b= b, a
    print(int(a * b /EA(a, b)))
    

## ��Ŭ���� ȣ���� -> �ּҰ����, �ִ����� ���ϴ� ��****