import sys
input = sys.stdin.readline

a = int(input())
s = input().split()
b = (int(x) for x in s)
nums = [0] * (a+1)
visitd = []
def run():
    for i in b:
        if not nums[i]:
            nums[i] = 1
            visitd.append(i)
        else:
            if visitd.pop() != i:
                return False
    return True

if run():
    print('YES')
else:
    print('NO')