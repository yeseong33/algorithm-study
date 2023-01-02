from cmath import sqrt
import sys

while True:
    nums = list(map(int, sys.stdin.readline().split()))
    z = list(map(lambda x: x**2, nums))
    c = max(z)
    z.remove(c)
    a = z[0]
    b = z[1]
    
    if a == 0 and b == 0 and c == 0:
        break    
    
    if a + b == c:
        print('right')
    else:
        print('wrong')
        
    

    