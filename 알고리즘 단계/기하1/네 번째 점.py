import sys

a = []
b = []
s = ''
for i in range(3):
    x, y = map(int, sys.stdin.readline().split())
    a.append(x)
    b.append(y)
    
for i in a:
    if a.count(i) == 1:
        s += str(i)
           
for i in b:
    if b.count(i) == 1:
        s += ' '+ str(i)
        
print(s)