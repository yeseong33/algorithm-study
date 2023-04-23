# 한 값을 설정하고 이후에 two pointer를 여러번 사용함
import sys
# 무한의 값 - 문제 조건에 따라 크기 정할 것
INF = int(1e10)

# 입력값
n = int(input())
nums = list(map(int, sys.stdin.readline().split()))

# 정렬을 진행해야 이후 투포인터 사용 시 포인터의 이동을 결정할 수 있다. 
# 값이 작아 져야 할 경우 - right 줄임 
# 값이 커져야 할 경우 - left 키움
nums.sort()

# 투 포인터 구현
def pointer():
    # 어떤 값과 다른 두 값을 더해 어떤 값과 같은 지를 카운트
    count = 0 
    
    # nums의 각 원소에 대해 투포인터를 실행
    # range - 현재 포인터의 값과 fix 된 인덱스가 같은지 확인하려 함 
    for i in range(n):
        # 다른 두 값을 더해 나와야 하는 값
        fix = nums[i]
        
        # 포인터 위치 초기화
        left = 0
        right = n-1
        
        # 포인터가 움직임
        # left == right 되는 순간 그 이후에 되는 값은 비교할 필요 없음
        # 정렬을 한 뒤 포인터를 움직이므로 가능한 조합이 다 나온 것
        while left < right:
            # nums의 각 포인터의 값을 더함
            sum = nums[left] + nums[right]
            # sum과 fix가 같고
            if sum == fix:
                # 포인터가 fix의 인덱스와 다르면
                # 다른 값을 더해 나온 값이 sum == fix 이면
                if left != i and right != i: 
                    # 그 값이 Good이 될 수 있음
                    count += 1
                    # good이 될 수 있는지만 판별하면 되므로 이후엔 그 
                    # 투포인터를 더이상 진행할 필요가 없음
                    break
                # 만약 값은 같은데 fix의 인덱스가 포함되어 있다면
                # 그 포인터를 이동시켜줌
                elif left == i:
                    left += 1
                elif right == i:
                    right -= 1
                    
            # sum이 fix 값보다 크면
            # 값을 줄여줘야 함 - 정렬된 상태에서 right를 줄여야 sum 값이 줄어듦
            if sum > fix:
                right -= 1
            # right의 경우와 반대
            elif sum < fix:
                left += 1
    # nums의 각 원소에 대해 투포인터를 적용한 후 good으로 count된 값을 반환
    return count

# 함수를 실행후 return 값을 c로 받음
c = pointer()
# c를 출력
print(c)