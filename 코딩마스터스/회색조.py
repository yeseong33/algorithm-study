import sys
input = sys.stdin.readline

s = list(input().strip()[1:])

for i in range(0, 6):
    if i%2==0:
        if not s[i].isdigit():
            s[i] = (ord(s[i])-55) * 16
        else:
            s[i] = int(s[i])* 16
    else:
        if not s[i].isdigit():
            s[i] = (ord(s[i])-55)
        else:
            s[i] = int(s[i])

r, g, b = s[0]+s[1], s[2]+s[3], s[4]+s[5]
avg = round((r+g+b)/3)
a = avg//16
b = avg%16
if a >= 10:
    a = chr(a+55)
if b >= 10:
    b = chr(b+55)
print("#"+(str(a)+str(b))*3)