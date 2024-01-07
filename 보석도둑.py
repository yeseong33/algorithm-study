import sys
sys.setrecursionlimit(10**6)
n, k = map(int, sys.stdin.readline().split())
nums = [0] * 300001
j = []
for i in range(n):
    m, v = map(int, sys.stdin.readline().split())
    j.append([m, v])

j.sort(key = lambda x: x[1])

count = k
bag = []
for i in range(k):
    tmp = int(sys.stdin.readline())
    bag.append(tmp)
    nums[tmp] = 1
bag.sort()
now = -1
for i in range(300000, -1, -1):
    if nums[i] == 1:
        now = i
    if now != -1:
        if nums[i] == 0:
            nums[i] = now
nums[0] = 0 
def find(n):
    global nums
    if nums[n] == 0:
        return 0
    elif nums[n] == 1:
        return n
    else:
        t = find(nums[n])
        if t == 0:
            nums[n] = 0
        return t
total =0 
while count:
    if j == []:
        break
    m, v = j.pop()
    if nums[m] > 0:
        x = find(m)
        if nums[x] == 1:
            if nums[x+1] == 0:
                nums[x] = 0
                while True:
                    if nums[x] == 1:
                        break 
                    nums[x] = 0
                    x -= 1
                    if x == 0:
                        break
            else:
                nums[x] = x+1
            count -= 1
            total += v
    print(nums[1:10])
print(total)
# 3 6
# 6 12
# 5 10
# 5 4
# 1
# 2
# 3
# 4
# 6
# 7

# 3 5
# 6 12
# 5 10
# 8 4
# 1
# 2
# 3
# 4
# 6