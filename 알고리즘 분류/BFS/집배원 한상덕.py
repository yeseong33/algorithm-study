# 우체국과 집을 찾음
# 이때 이를 리스트로 만듦
# 가장 큰 값과 작은 값을 설정
# 움직일 수 있는 것을 구현
import sys

n = int(input())

town = []
hight = []

for i in range(n):
    k = list(sys.stdin.readline().strip())
    town.append(k)

for i in range(n):
    k = list(map(int, sys.stdin.readline().split()))
    hight.append(k)


# for i in town:
#     print(* i)

# for i in hight:
#     print(*i)

mini = int(1e10)
max = 0


for i in range(n):
    for j in range(n):
        tmp = town[i][j]
        if tmp != '.':
            if hight[i][j] < mini:
                mini = hight[i][j]
            if hight[i][j] > max:
                max = hight[i][j]
                
print(max-mini)