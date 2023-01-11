import sys
n = int(input())

nums = []

for i in range(n):
    k =list(map(int, sys.stdin.readline().split()))
    nums.append(k)

nums.sort(key = lambda x: (x[1], x[0]))
count = 1
end = nums[0][1]

for i in range(1, n):
    if nums[i][0] >= end:
        end = nums[i][1]
        count += 1 


print(count)