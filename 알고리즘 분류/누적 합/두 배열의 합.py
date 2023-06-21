import sys

t = int(input())

n = int(input())
A = list(map(int, sys.stdin.readline().split()))

m = int(input())
B = list(map(int, sys.stdin.readline().split()))

A_hap = [0] * (n+1)
B_hap = [0] * (m+1)

total = 0
for i in range(1, n+1):
    total += A[i-1]
    A_hap[i] = total

total = 0
for i in range(1, m+1):
    total += B[i-1]
    B_hap[i] = total

able_V = dict()
for i in range(1, n+1):
    start = 0
    end = start + i
    
    while end < n+1:
        value = A_hap[end] - A_hap[start]
        if value not in able_V:
            able_V[value] = 1
        else:
            able_V[value] += 1
        start += 1
        end += 1

count = 0
able_v_b = dict()
for i in range(1, m+1):
    start = 0
    end = start + i
    
    while end < m+1:
        value = t - (B_hap[end] - B_hap[start])
        if  value in able_V:
            count += able_V[value]
        start += 1
        end += 1

print(count)

