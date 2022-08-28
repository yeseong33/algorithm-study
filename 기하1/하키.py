import sys
from tkinter import W 

w, h, a, b, p = map(int, sys.stdin.readline().split())
r = h//2
c = 0

for i in range(p):
    x, y = map(int, sys.stdin.readline().split())
    if x <= a  and (x -a)**2 + (y-(b+r))**2 <= r**2:
        c += 1
    elif a < x < a + w and b <  y < b + h:
        c += 1
    elif x >= a + w  and (x -(a+w))**2 + (y-(b+r))**2 <= r**2:
        c += 1
print(c)        
        
        
        