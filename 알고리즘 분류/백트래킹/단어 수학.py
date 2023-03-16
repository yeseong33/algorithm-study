import sys

n = int(input())

nums = []

for i in range(n):
    k = list(map(str, sys.stdin.readline().strip()))
    t = 8-len(k)
    nk = [0] * t + k
    nums.append(nk)


pro = []
visited = []

alph = [0] * 28

for i in range(n):
    for j in range(8):
        # 값이 알파벳인지 검사
        if nums[i][j] != 0:
            al = ord(nums[i][j]) -65
            
            # 값이 이미 존재하면 값에 현재 자리수를 더해줌
            if alph[al] == 0:
                alph[al] = 10 ** (7-j)
            else:
                alph[al] += 10 ** (7-j)
                
values = []

for i in alph:
    if i != 0:
        values.append(i)
        
values.sort(reverse=True)

total = 0
k = 9

for i in values:
    total += i * k
    k -= 1
    
print(total)
