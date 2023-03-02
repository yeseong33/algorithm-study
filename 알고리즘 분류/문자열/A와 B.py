import sys

s = input()
t = input()

s_count = len(s) -1
point = len(t)-1

while point != s_count:
    
    if t[point] == 'A':
        t = t[:point]
        point -=1
    elif t[point] == "B":
        t = t[:point]
        t = t[-1::-1]
        point -= 1
if t == s:
    print(1)
else:
    print(0)
    