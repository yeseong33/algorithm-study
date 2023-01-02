import sys
n= int(sys.stdin.readline())
nums = list(map(int, sys.stdin.readline().split()))

nums.sort()
ans = 0
temp = 0

for i in range(n):
    temp += nums[i]
    ans += temp
    print(ans)
print(ans)

# 1 2 3 3 4

# 1 3 6 9 13