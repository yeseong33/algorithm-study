
import sys


def test(n):
    nums = []
    for i in range(n):
        nums.append(list(map(int, sys.stdin.readline().split())))
    nums.sort()
    
    rank = []
    for i in nums:
        rank.append(i[1])
        
    m = rank[0]
    count = 1
    
    for i in rank:
        if i < m:
            m = i 
            count += 1         
    print(count)
        
    
    
    

t = int(input())

for i in range(t):
    n = int(input())
    test(n)
   
   

