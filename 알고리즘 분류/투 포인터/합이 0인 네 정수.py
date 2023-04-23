import sys

# 배열의 크기
n = int(input())

# A, B, C, D 배열을 받는다. 
# A+B, C+D 의 값을 차례로 받는다. 
# -> ab의 값과 cd의 값을 더해서 0인 수를 세면
# (a, b, c, d)가 0이 되는 개수를 구할 수 있다. 

# A+B, C+D 배열
a1 = []
a2 = []

# 입력값을 받으면서 바로 a1, a2를 계산
# 계산 시간을 줄일 수 있다.
arr = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]

for i in range(n):
    for j in range(n):
        a1.append(arr[i][0] + arr[j][1])
        a2.append(arr[i][2] + arr[j][3])

# 이를 정렬 
a1.sort()
a2.sort()

# 투 포인터 사용
def point(a1, a2):
    # 시작 인덱스 위치
    p1 = 0
    p2 = len(a2)-1
    # 길이 -> 종료시점을 위함(범위)
    lenth = len(a2)
    # 0인 값을 셈
    count = 0 
    
    # 리스트 보다 커지거나 작아지는 순간 멈추도록
    while p1 < lenth and p2 >= 0:
        # 두 값의 합
        sum = a1[p1] + a2[p2]
        # 0이라면 
        if sum == 0:
            # 다음 인덱스의 값 설정
            # 같은 수가 있을 수 있으므로 이를 고려해야 함
            nextP1 = p1 + 1  
            nextP2 = p2 - 1 
            # 커지는 포인터의 개수
            while nextP1 < lenth and a1[p1] == a1[nextP1]:
                nextP1 += 1
            # 작아지는 포인터의 개수
            while nextP2 >= 0 and a2[p2] == a2[nextP2]:
                nextP2 -= 1
            # 두 포인터가 몇개가 겹치는지 계산
            count += (nextP1 - p1) * (p2 - nextP2)
            # 포인터의 위치 조정
            p1, p2 = nextP1, nextP2
        # 두 값이 0보다 크면 값이 작아지는 방향으로 가야함
        # p2의 인덱스 줄여야 값이 작아짐
        # 여기서 범위를 고려하지 않는 이유
        # -> 어떤 값이 끝 인덱스에 도달했을 때 더이상 다른 조합을 고려할
        # 필요가 없음
        elif sum > 0:
            p2 -= 1
        else:
            p1 += 1
    return count

print(point(a1, a2))
            