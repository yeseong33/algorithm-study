import sys

n, k = map(int, sys.stdin.readline().split())

nums = [0]
result = []
arr = list(map(int, sys.stdin.readline().split()))
t = 0
max_num = -101 * n
 
for i in arr:
    t += i
    nums.append(t)


for i in range(n-k+1):
    ans = nums[k+i] - nums[i]
    if ans > max_num:
        max_num = ans


if n == k:
    print(sum(arr))
else:
    print(max_num)


# 누적 합을 이용
# 부분합을 구할때 nums의 index가 k만큼 차이나면 부분합에
# 참여하는 수도 k이다.
