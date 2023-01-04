import sys

n, m = map(int, sys.stdin.readline().split())

nums = [[0]*(m+1)]
arr = []

for i in range(n):
    k = list(map(int, sys.stdin.readline().split()))
    arr.append(k)
    nums.append([0]*(m+1))

for i in range(1, n+1):
    for j in range(1, m+1):
        nums[i][j] = arr[i-1][j-1] + nums[i-1][j] + nums[i][j-1] - nums[i-1][j-1]

k = int(sys.stdin.readline())

for i in range(k):
    x1, y1, x2, y2 = map(int, sys.stdin.readline().split()) 
    ans = nums[x2][y2] - nums[x2][y1-1] - nums[x1-1][y2] + nums[x1-1][y1-1]
    print(ans)
