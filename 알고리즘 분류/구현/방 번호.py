import sys
nums = list(map(int,sys.stdin.readline().strip()))

n_set = [1] * 10
n_set[6] += 1
n_set[9] += 1
count = 1
for i in range(len(nums)):
    tmp = nums[i]
    if n_set[tmp] == 0:
        for j in range(10):
            if j == 6 or j == 9:
                n_set[j] += 2
            else:
                n_set[j] += 1
        count += 1
        
    if tmp == 6 or tmp == 9:
        n_set[6] -= 1
        n_set[9] -= 1
    else:
        n_set[tmp] -= 1
print(count)