import sys

n, m = map(int, input().split())

nums = []

for _ in range(n):
    k = list(map(int, sys.stdin.readline().split()))
    nums.append(k)
    
i = 0 
j = 0

ans = 0     


# (1) 막대기

while True:
    total = nums[i][j] + nums[i][j+1] + nums[i][j+2] + nums[i][j+3]  
    
    if ans <= total:
        ans = total
    if i == n-1 and j+3 == m-1:
        i = 0 
        j = 0
        break
    elif j+3 == m-1:
        i +=1
        j = 0 
    else:
        j += 1
        
while True:
    total = nums[i][j] + nums[i+1][j] + nums[i+2][j] + nums[i+3][j] 
    if ans <= total:
        ans = total
    if i+3 == n-1  and j == m-1:
        i = 0
        j = 0 
        break
    elif j == m-1:
        i +=1
        j = 0 
    else:
        j += 1

#(2) 네모

while True:
    total = nums[i][j] + nums[i][j+1] + nums[i+1][j] + nums[i+1][j+1] 
    if ans <= total:
        ans = total
    if i+1 == n-1  and j+1 == m-1:
        i = 0
        j = 0 
        break
    elif j+1 == m-1:
        i +=1
        j = 0 
    else:
        j += 1

#(3) ㄱ, ㅗ, Z
#세로
while True:
    total_1 = nums[i][j] + nums[i][j+1] + nums[i+1][j+1] + nums[i+2][j+1] 
    total_2 = nums[i][j] + nums[i+1][j] + nums[i+2][j] + nums[i+2][j+1]
    total_3 = nums[i][j] + nums[i][j+1] + nums[i+1][j] + nums[i+2][j]
    total_4 = nums[i][j+1] + nums[i+1][j+1] + nums[i+2][j] + nums[i+2][j+1]
    total_5 = nums[i][j] + nums[i+1][j] + nums[i+1][j+1] + nums[i+2][j+1]
    total_6 = nums[i][j+1] + nums[i+1][j+1] + nums[i+1][j] + nums[i+2][j]
    total_7 = nums[i][j] + nums[i+1][j] + nums[i+2][j] + nums[i+1][j+1]
    total_8 = nums[i][j+1] + nums[i+1][j+1] + nums[i+2][j+1] + nums[i+1][j]
    
    ans = max(ans, total_1, total_2, total_3, total_4, total_5, total_6, total_7, total_8)
    
    if i+2 == n-1  and j+1 == m-1:
        i = 0
        j = 0 
        break
    elif j+1 == m-1:
        i +=1
        j = 0 
    else:
        j += 1


#가로
while True:
    total_1 = nums[i][j] + nums[i][j+1] + nums[i][j+2] + nums[i+1][j] 
    total_2 = nums[i][j] + nums[i][j+1] + nums[i][j+2] + nums[i+1][j+2]
    total_3 = nums[i][j+2] + nums[i+1][j] + nums[i+1][j+1] + nums[i+1][j+2]
    total_4 = nums[i][j] + nums[i+1][j] + nums[i+1][j+1] + nums[i+1][j+2]
    total_5 = nums[i][j] + nums[i][j+1] + nums[i+1][j+1] + nums[i+1][j+2]
    total_6 = nums[i+1][j] + nums[i+1][j+1] + nums[i][j+1] + nums[i][j+2]
    total_7 = nums[i][j] + nums[i][j+1] + nums[i][j+2] + nums[i+1][j+1]
    total_8 = nums[i][j+1] + nums[i+1][j] + nums[i+1][j+1] + nums[i+1][j+2]
    ans = max(ans, total_1, total_2, total_3, total_4, total_5, total_6, total_7, total_8)
    
    if i+1 == n-1  and j+2 == m-1:
        i = 0
        j = 0 
        break
    elif j+2 == m-1:
        i +=1
        j = 0 
    else:
        j += 1


print(ans)
