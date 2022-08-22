import sys

n = int(sys.stdin.readline())

ns = list(map(int,sys.stdin.readline().split()))

m = int(sys.stdin.readline())
 
ms = list(map(int,sys.stdin.readline().split()))


ns_d = {}
for i in ns:
    ns_d[i] = 0
    

for i in ms:
    if i in ns_d:
        print(1, end = ' ')
    else:
        print(0, end = ' ')
        


###
# a in b , a not in b 연산을 할경우 
# 리스트: O(N)
# 집합, 딕셔너리: O(1)
