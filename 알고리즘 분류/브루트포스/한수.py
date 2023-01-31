def hanSu():
    n = int(input())
    nums = 0
    
    for i in range(1, n+1):
        arr = [(i//(10**j))%10 for j in range(len(str(i)))]
        if i >= 10:
            diff = arr[0] - arr[1]
            for k in range(len(arr)-1):
                if arr[k]-arr[k+1] != diff:
                    nums -= 1
                    break
        nums += 1 
    print(nums)

hanSu()

import cProfile

cProfile.run("hanSu()")
        
        
        
# 코드 리펙토링 해서 더 짧고 깔끔하게 만듦
# 이전 풀이 보다 속도 개선 