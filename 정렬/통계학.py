import sys

n = int(input())

nums = [int(sys.stdin.readline().strip()) for i in range(n)]
nums.sort()
num = {}

for i in nums:
    if i in num:
        num[i] += 1
    else:
        num[i] = 1

s = []
m = 0
for i in num.keys():
    v = num[i]
    if v > m:
        m = v
        s.clear()
        s.append(int(i))
    elif v == m:
        s.append(int(i))

s.sort()



san_avg = int(round(sum(nums)/n,0))
mid_avg = nums[n//2] 

def most_avg():
    if len(s) > 1:
        return s[1]
    else:
        return s[0]

range_avg = max(nums)-min(nums)



print(san_avg)
print(mid_avg)
print(most_avg())
print(range_avg)
