import sys

n = int(sys.stdin.readline())
if n == 1:
    print(0)
elif n == 2:
    print(1)
elif n == 3:
    print(2)
else:
    nums = [0, 2, 4]
    for i in range(3, n//2+1):
        tmp = nums[i-1]+i
        if tmp >= n:
            print(i)
            break
        nums.append(nums[i-1]+i)