from sys import stdin as ss

ss = open('C:\\Users\\yeseong\\code\\algorithmstudy\\코딩마스터스\\input.txt')

x, y, z = map(int, ss.readline().split())

def check(a, b, c):
    if a==b and b!=c:
        if a > c:
            return True
        else:
            return False

if check(x, y, z) or check(y, z, x) or check(z, x, y):
    print('possible')
else:
    print('impossible')
