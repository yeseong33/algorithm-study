import sys

prices= int(sys.stdin.readline())
n= int(sys.stdin.readline())
acc = 0

for i in range(n):
    price, amount  = map(int, sys.stdin.readline().split())
    acc += price * amount

if prices == acc:
    print("Yes")
else:
    print("No")
    
