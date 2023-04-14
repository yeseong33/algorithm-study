import sys

# 입력값 받기
n = int(input())

# 받은 용액으로 리스트 만들기
lq = list(map(int, sys.stdin.readline().split()))
# 투포인터를 사용하기 위해 정렬(NlogN)
lq.sort()

# 투포인터 구현
def point(left, right):
    # 현재 포인터의 두 값을 더할 sum
    sum = 0 
    # 가장 0에 가까운 인덱스 페어를 저장
    ans = [left, right]
    # 가장 0에 가까운 값을 저장
    to_zero = abs(lq[left] + lq[right])
    
    # 두 포인터가 같아지면 더이상 고려할 조합이 없음
    while left != right:
        # 현재 포인터의 두 값의 합
        sum = lq[left] + lq[right]
        # 현재 포인터의 두 값의 합의 절대값 - 0에 가까워야 함
        abs_sum = abs(sum)
        # 0에 가장 가까운 것을 출력하는 것
        # 0일 경우 함수를 멈추고 그값을 반환
        if sum == 0:
            ans = [left, right]
            break
        else:
            
            if to_zero > abs_sum:
                to_zero = abs_sum
                ans = [left, right]
            # 현재 두 포인터의 합의 음, 양에 따라 나눔
            # 음수일 경우 - 값이 0으로 가려면 음수의 값이 작아져야 함
            if sum < 0:
                left += 1
            # 양수일 경우 - 값이 0으로 가려면 양수의 값이 작아져야 함
            elif sum > 0:
                right -= 1
    # 0에 가장 가까운 값을 리턴
    return ans

ans = point(0, n-1)
# 인덱스 형태로 받아와지기 때문에 lq에 넣어 실제 값을 오름차순으로 출력
print(lq[ans[0]], lq[ans[1]])

# -99 -2 -1 4 98
# 값이 음수고
# 절대값이 작으면
# 값이 양수고 
# 절대값이 작으면