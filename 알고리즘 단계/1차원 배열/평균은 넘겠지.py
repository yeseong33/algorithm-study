import sys
n = int(sys.stdin.readline())

for i in range(n):
    l = list(map(int, sys.stdin.readline().split()))
    num = l[0]
    sum_all = sum(l[1:])
    avg = sum_all/num
    count = 0
    for i in range(1, len(l)):
        if l[i] > avg:
            count += 1
    ratio = format(count/num*100, '.3f')
    print(ratio, '%', sep = '')    
        
