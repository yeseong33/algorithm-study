import sys

n, m = map(int, sys.stdin.readline().split())
nums = list(map(int, sys.stdin.readline().split()))


def black(nums, m):
    n = len(nums)
    maxi = [0 for i in range(n)]
    for i in range(n):
        for j in range(i+1, n):
            for k in range(j+1, n):
                b = [nums[i], nums[j], nums[k]]
                if sum(b) == m:
                    maxi = b
                    break
                elif sum(maxi) < sum(b) < m:
                    maxi = b.copy()
    
    return maxi

print(sum(black(nums, m)))
                