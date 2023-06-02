import sys

n = int(input())

m = int(input())

# m이 0이면 고장난 숫자값이 입력되지 않음
if m != 0:
    broken = list(map(int, sys.stdin.readline().split()))
else:
    broken = []

# +, -으로만 움직였을 때 최소값
min_count = abs(100-n)

# 1000000까지 채널에서 구함
for nums in range(1000001):
    # 입력값을 str으로 변환
    nums = str(nums)
    # 입력값의 자리 수만큼 for
    for j in range(len(nums)):
        # 입력값의 자리 수에서 고장난 값이 있으면 그 채널은 못감
        if int(nums[j]) in broken:
            break
        # 이동 가능한 채널이면
        if j == len(nums)-1:
            # abs(int(nums) -n) -> +, -로 이동할 값
            # len(nums) -> 번호를 눌러 이동할 값
            min_count = min(min_count, abs(int(nums) - n) + len(nums))
            
print(min_count)
        