import sys

n, s = map(int, sys.stdin.readline().split())

nums = list(map(int, sys.stdin.readline().split()))

hap = [0] * (n+1)
total = 0

for i in range(1, n+1):
    total += nums[i-1]
    hap[i] = total

start = 0
end = 1
min_len = 10**9 + 1

while end < len(hap):
    value = hap[end] - hap[start]
    
    if value >= s:
        if min_len > end - start:
            min_len = end -start
        start += 1
    else:
        end += 1

if min_len == 10 ** 9 +1:
    print(0)
else:
    print(min_len)