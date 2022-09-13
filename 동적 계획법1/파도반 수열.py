t = int(input())



def P(n):
    if n > 10:
        for i in range(10, n):
            p[i] = p[i-3] + p[i-2]
        
        print(p[-1])
    else:
        print(p[n-1])


for i in range(t):
    n = int(input())
    p = [1, 1, 1, 2, 2, 3, 4, 5, 7, 9] + [0] * (n-10)
    P(n)