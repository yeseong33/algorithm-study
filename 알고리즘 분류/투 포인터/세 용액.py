# 용액에 대해서 가능한 조합을 모두 구함
# sort
# 

import sys

n = int(input())

nums = list(map(int, sys.stdin.readline().split()))

nums.sort()



def point():
    min_sum = int(1e10)
    ans = []
    for fix in range(n-2):   
    
        left  = fix + 1
        right = n-1

        while left < right:
            sum = nums[left] + nums[fix] + nums[right]
            to_zero = abs(sum)
            

            if sum == 0:
                ans = [left, fix, right]
                return ans
            else:
                
                if to_zero < min_sum:
                    min_sum = to_zero
                    ans = [left, fix, right]

                if sum > 0:
                    right -= 1                
                elif sum < 0:
                    left += 1
  
            
                
    return ans


r = point()

rr = []
for i in r:
    rr.append(nums[i])
    
rr.sort()
print(*rr)
