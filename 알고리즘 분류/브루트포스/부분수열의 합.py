import sys

n, s = map(int, sys.stdin.readline().split())

nums = list(map(int, sys.stdin.readline().split()))

total = 0 
count = 0 

def hap(idx):
    global count, total
    
    
    if total == s and idx != 0:
        count += 1
    
    
    for i in range(idx, n):
        total += nums[i]
        hap(i+1)
        total -= nums[i]
        

            
hap(0)
print(count)