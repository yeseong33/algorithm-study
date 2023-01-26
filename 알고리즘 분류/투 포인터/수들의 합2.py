import sys

n, m = map(int, sys.stdin.readline().split())
arr = list(map(int, sys.stdin.readline().split()))
nums = [0]

start = 0
end = 0
count = 0

k = 0 
for i in arr:
    k += i
    nums.append(k)

# 0 1 1 1 1

while True:
    
    result = nums[end] - nums[start]
        
    if result == m:
        count += 1
    
    if result >= m:
        start += 1
    elif result < m :
        if end < n:
            end += 1
        else:
            start += 1
        
    if start == n:
        break
        
print(count)
         