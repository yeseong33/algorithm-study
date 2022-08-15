import sys 

n = int(sys.stdin.readline())

nums = 1
for i in range(n):
    if n / nums <= 1:
        if (i+1) % 2 == 1:
            num = nums % n + 1
            a = num
            b = (i+2) - a
            print(str(a) + '/'+ str(b))
            break
        else:
            num = nums % n + 1
            b = num
            a = (i+2) -b 
            print(str(a) + '/'+ str(b))
            break 
    nums += (i+2)
    