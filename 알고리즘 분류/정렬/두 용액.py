import sys

n = int(input())

a = []
b = []

temp = list(map(int, sys.stdin.readline().split()))

for i in range(n):
    k = temp.pop()
    if k > 0:
        a.append(k)
    else:
        b.append(k)
a.sort(reverse=True)
b.sort()




if a == [] or b == []:
    r = a + b
    if r[0] >0:
        r.sort()
    else:
        r.sort(reverse=True)
    r = r[:2]
    print(*r)
elif len(a)== 1 and len(b)== 1:
    r = a+b
    r.sort()
    print(*r)
else:
    i = 0
    j = 0
    to_zero = 1000000001
    
    
    ## 맨 앞에 두개가 될 가능성
    ## 3개일 때 처리 
    if len(a) >= 2 and len(b) == 1:
        to_zero = sum(a)
        ans = [a[1], a[0]]
    elif len(b) >= 2 and len(a) == 1:
        to_zero = sum(b)
        ans = [b[0], b[1]]
    else:
        a_sum = sum(a[len(a)-2:])
        b_sum = abs(sum(b[:2]))
        
        if a_sum < b_sum:
            to_zero = a_sum
            ans = [a[-1], a[-2]]
        else:
            to_zero = b_sum
            ans = [b[0], b[1]]
   
     

    while True:
        if i == len(a)-1 and j == len(b)-1:
            break

        
        x = a[i]
        y = b[j]

        spic = abs(x+y)
        
        
        if spic <= to_zero:
            to_zero = spic
            ans = [x, y]
            if i == len(a)-1:
                j += 1
            else:
                i += 1
        
        elif spic > to_zero:
            if j == len(b)-1:
                i+= 1
            else:
                j += 1

    if to_zero > abs(a[-1] + b[-1]):
        to_zero = abs(a[-1] + b[-1])
        ans = [a[-1], b[-1]]
    ans.sort()
    print(*ans)    
                




# 5
# -1 -2 -3 -4 -5

# 7
# -99 -2 -1 1 98 100 101
# 5
# 1 2 3 4 5
# 6
# -99 -60 3 7 61 130



stack = []
