alphanumeric = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ\$%*+-./:"

import sys

n = int(sys.stdin.readline())
for i in range(n):
    R, S = sys.stdin.readline().split()
    l = list(map(str, S))
    s = ''
    for j in range(len(l)):
         s += l[j] * int(R)
    print(s)  
    


## string 의 성질 잘 이용 해야 함
for i in range(n):
    r, s = sys.stdin.readline().split()
    for i in s:
        print(int(r)*j, end='')
    print()