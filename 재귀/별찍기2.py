import math

def star(n):
    s = []
    if n==1:
        s.append('***')
        s.append('* *')
        s.append('***')
        
    if n>=2:
        t = star(n-1)
        for i in range(len(t)):
            s.append(t[i]*3)
        for i in range(len(t)):
            s.append(t[i] + ' '*(3**(n-1)) + t[i])
        for i in range(len(t)):
            s.append(t[i]*3)
    return s

num = int(input())
n = math.ceil(math.log(num,3))

s = star(n)
for i in range(len(s)):
    print(s[i])