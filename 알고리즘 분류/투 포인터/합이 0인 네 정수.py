import sys

n = int(input())

A = [0] * n
B = [0] * n
C = [0] * n
D = [0] * n

for i in range(n):
    a, b, c, d = map(int, sys.stdin.readline().split())
    A[i], B[i], C[i], D[i] = a, b, c, d
    
A.sort()
B.sort()
C.sort()
D.sort()



def point(l1, l2):
    l1.sort()
    l2.sort()
    count = 0
    p1 = 0
    p2 = n-1
    
    print(l1, l2)
    
    while p1 != n-1 or p2 != 0:
        
        sum = l1[p1] + l2[p2]
        print(sum)
        if sum == 0:
            count += 1
            if p1 != n-1:
                p1 += 1
            else:
                p2 -= 1
        elif sum < 0:
            if p1 != n-1:
                p1 += 1
            else: 
                p2 -= 1
        elif sum > 0:
            if p2 != 0:
                p2 -= 1
            else: 
                p1 += 1
    return count

c = point([-45, -41, -36, -36, 26, -32], [22, -27, 53, 30, -38, -54])
c1 = point([-45, -41, -36, -36, 26, -32], [42, 56, -37, -75, -10, -6])
c2 = point([-45, -41, -36, -36, 26, -32], [-16, 30, 77, -46, 62, 45])
print(c, c1, c2)


            
        













# lists = [A, B, C, D]

# for i in range(1, 4):
    
    