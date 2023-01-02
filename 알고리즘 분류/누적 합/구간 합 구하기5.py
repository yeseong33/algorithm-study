import sys
n, m = map(int, sys.stdin.readline().split())

arr = []
nums = [[0]*(n+1)]

    
for i in range(n):
    arr.append(list(map(int, sys.stdin.readline().split())))
    nums.append([0]*(n+1))

for i in range(1, n+1):
    for j in range(1, n+1):
        nums[i][j] = arr[i-1][j-1] + nums[i][j-1] +nums[i-1][j] - nums[i-1][j-1]

print(nums)
# [[0, 0, 0, 0, 0],
#  [0, 1, 3, 6, 10],
#  [0, 3, 8, 15, 24],
#  [0, 6, 15, 27, 42],
#  [0, 10, 24, 42, 64]]

for _ in range(m):
    x1, y1, x2, y2 = map(int, sys.stdin.readline().split())

    ans = nums[x2][y2] -nums[x2][y1-1] - nums[x1-1][y2] + nums[x1-1][y1-1]
    print(ans)


# for _ in range(m):
#     x1, y1, x2, y2 = map(int, input().split())

#     ans = 0

#     for x in range(x1, x2+1): 
#         ans += nums[x][y2] - nums[x][y1-1]
#     print(ans)
    
# 최악의 경우에 n*m이 걸린다. 따라서 옮지 않음
# ans를 구하는 부분에서 시간 초과 발생
# 이를 해결해야 함


