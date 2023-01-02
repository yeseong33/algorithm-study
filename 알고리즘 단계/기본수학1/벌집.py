num = int(input())
nums = 1
k = 2

if num == 1:
    print(1)
else:  
    while num / nums > 1:
        nums += 6*k -6
        k += 1
    k -= 1
    print(k)
        
        