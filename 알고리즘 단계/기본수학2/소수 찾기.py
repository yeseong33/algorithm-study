import sys

n = int(sys.stdin.readline())

nums = list(map(int, sys.stdin.readline().split()))
r = 0

for num in nums:
    count = 0
    for i in range(2, num):
        if num % i == 0:
            count += 1
    if count == 0 and num != 1:
        r += 1
print(r)

