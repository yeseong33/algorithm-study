import sys

n, m = map(int, sys.stdin.readline().split())

nums = list(map(int, sys.stdin.readline().split()))
nums.sort(reverse=True)
nums_c = [len(str(i)) for i in nums]
memori = sum(nums_c) + n-1


def convert(value, n, N):
    new_n = n
    for i in range(8):
        if N ** i <= value < N ** (i+1):
            new_n = i+1
            break
    return new_n, n-new_n

def run(n, m, memori):
    for now in range(11, 63):
        for i in range(n):
            a, b = convert(nums[i], nums_c[i], now)
            nums_c[i] = a
            memori -= b
            if memori <= m:
                print(now)
                return
    print(-1)
    
if memori <= m:
    print(10)
else:
    run(n,m,memori)





            