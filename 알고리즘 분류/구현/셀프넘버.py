def solution():
    nums = [0] * 11000
    
    def make(n):
        k = str(n)
        ans = n
        for i in k:
            ans += int(i)
        return ans 
    
    for i in range(1, 10001):
        nums[make(i)] = 1
        
    for idx, i in enumerate(nums[1:10001]):
        if i == 0:
            print(idx+1)
    return

solution()