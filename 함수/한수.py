import sys
import cProfile

def han():
    n = int(sys.stdin.readline())
    count = 0
    for i in range(1, n+1):
        N = str(i)
        if i < 100:
            count += 1
        elif 1000 > i >= 100:
            a, b, c = map(int, N)
            if 2*b == a+c and a != c or a == b == c:
                count += 1
    print(count)           
            

# cProfile.run("han()")