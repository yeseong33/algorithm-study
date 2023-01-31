# 1. 키가 작은 순서로 정렬함
# 2. 순차적으로 더해나감
# 3. 100 보다 작을 경우 가장 끝에 있는 수를 한칸 옮김
# 4. 깊이 우선 탐색 사용

import sys

short = []
for i in range(9):
    k = int(sys.stdin.readline())
    short.append(k)
    
short.sort()
temp = []
ans = []
count = 0 

def dfs():
    global count, ans
    if count == 1:
        return
    
    if len(temp)== 7:
        if sum(temp) == 100:
            count += 1 
            ans = temp.copy()
            return
    else:
        for i in short:
            if i not in temp:
                temp.append(i)
                dfs()
                temp.pop()

dfs()
for i in ans:
    print(i)



