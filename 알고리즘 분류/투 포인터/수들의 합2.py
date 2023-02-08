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

# 백준 (수들의 합2, 2003)

# 누적합을 통해 수열의 합을 O(1)로 구할 수 있다. 
# 이후 문제에 맞게 조건식을 적어 문제 해결