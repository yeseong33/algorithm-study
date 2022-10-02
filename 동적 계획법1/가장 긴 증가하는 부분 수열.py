import sys

n = int(input())

nums = list(map(int, sys.stdin.readline().split()))
count = [1] * n


# answer
# 18 23 53 60 77 83 85

for i in range(n):
    for j in range(i):
        if nums[i] > nums[j]:
            if count[i] < count[j] + 1:
                 count[i] = count[j] + 1

print(count)       
print(max(count))       
            
            
# 다시풀기
