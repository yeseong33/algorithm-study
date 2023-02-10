
n = int(input())
i =1
ans = 0
count = 0

while True:
    ans += i
    if ans == n:
        print(i)
        break
    elif ans > n:
        print(i-1)
        break
    i +=1 
    
            
    
    