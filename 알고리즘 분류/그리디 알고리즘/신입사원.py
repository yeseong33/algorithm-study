# 1. 두 분야중 하나라도 일등이면 무조건 통과
# 2. sort 이후에 인덱스 1을 기준으로 낮으면 없앰
# 2중 for 사용



import sys


def test(n):
    nums = []

    for i in range(n):
        nums.append(list(map(int, sys.stdin.readline().split())))
    nums.sort()
    
    rank = []
    for i in nums:
        rank.append(i[1])
        
    count = 1
    
    m = rank[0]
    
    for i in rank:
        if i < m:
            m = i 
            count += 1         
    print(count)
        
    
    
    

t = int(input())

for i in range(t):
    n = int(input())
    test(n)
   
   


# 4 1
# 2 1
# 3 0 
# 1 1 
# 5 0 


# 1 4
# # 2 5
# # 3 6
# 4 2
# # 5 7
# 6 1
# 7 3