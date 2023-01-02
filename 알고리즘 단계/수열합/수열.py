import sys

n, k = map(int, sys.stdin.readline().split())
nums = list(map(int, sys.stdin.readline().split()))

temp = []
ans = []

for i in range(n):
    if temp != []:
        s = temp[-1] + nums[i]
    else:
        s = nums[i]
    temp.append(s)

# 미리 넣어줘야 함, -> 뒤에 처리 부분에서 
ans.append(temp[k-1])
for i in range(n-k):
        ans.append(temp[i+k]-temp[i])
    
# nums 1 2 3 
# temp 1 3 6
# ans  3 5


print(temp)
print(ans)

if n == k:
    print(sum(nums))
else:
    print(max(ans))

