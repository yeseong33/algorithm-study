# n이 주어졌을 때 소수를 먼저 구함
# 이후에 투포인터 기법을 통해 하나씩 증가시키면서 n이 되는지를 검사 
t = int(input())

# 에라토스테네스의 체
# 자신을 제외한 모든 배수를 제거
def makeSo(n):
    # 배수 여부를 체크할 리스트 
    visited = [False, False] + [True] * (n-1)
    # 2부터 체크
    for i in range(2, n+1):
        # 그 값이 아직 체크되지 않으면?
        # -> 소수의 가능성
        if visited[i]:
            # 배수에 대해 모두 방문처리
            for j in range(2*i, n+1, i):
                visited[j] = False
    # True인 값을 확인 
    # True의 의미
    # 자신을 제외한 배수중 중복되는 것이 없었다 -> 소수
    so = [i for i in range(n+1) if visited[i]]
    return so
    
# def check(n):
#     nums = makeSo(n)
#     right = 0
#     sum = 0
#     count = 0 
#     m = len(nums)
#     for left in range(m):
#         while sum < n and right < m:
#             sum += nums[right]
#             right += 1
#         if sum == n:
#             count += 1
#         sum -= nums[left]

        
#     return count

# 투포인터
def check(n):
    # 소수 리스트 만듦
    # index를 끝까지 확인하기 위한 +[0] -> while을 빠져나오기 위해 사용되는 조건
    nums = makeSo(n)+[0]
    # n과 같으면 체크
    count = 0 
    # 포인터
    right = 0
    left = 0
    # 총합 - 포인터를 기준으로 더해감
    sum = 0
    # [0]을 더해줬기 때문에 하나 빼줌
    lenth = len(nums)-1
    # right가 더 인덱스를 벗어날 때
    # 1. left가 동일한 위치
    # 2. left를 기준으로 더 더해도 더이상 n을 찾지 못할 때
    while right <= lenth:
        # sum 값이 찾는 값과 같음
        if sum == n:
            # 체크
            count += 1
            # left 포인터를 옮겨줬다 생각
            sum -= nums[left]
            left += 1
        # sum 값이 작으면
        elif sum < n:
            # 값을 키워야함
            # right에 대해 수행
            sum += nums[right]
            right += 1
        elif sum > n:
            # 값을 작게 만들어야 함
            # left에 대해 수행
            sum -= nums[left]
            left += 1
    return count

print(check(t))


# print(check(t))


# def ckeck(n):
#     count = 0
#     left = 0
#     right = 0
#     sum = 0
#     nums = [10, 1, 3, 6, 0]
#     lenth = len(nums)-1
#     while right <= lenth:
#         print(left, right)
#         print(sum)
#         if sum == n:
#             count += 1
#             sum -= nums[left]
#             left += 1
#         elif sum > n:
#             sum -= nums[left]
#             left += 1
#         elif sum < n:
#             sum += nums[right]
#             right += 1
#     return count

    