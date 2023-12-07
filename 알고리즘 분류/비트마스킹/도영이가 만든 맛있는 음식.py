import sys

nums=  [[] for _ in range(2**10+1)]

n = int(input())
min_diff = 10**9
# 2의 배수 값을 채움 -> 비트를 이용하기 위해 해당 값에 값을 채움
for i in range(n):
    idx = 2**i
    a, b = map(int, sys.stdin.readline().split())
    nums[idx] = [a, b]

# n길이 만큼의 비트 수가 필요
k = (1<<n)-1
# ex) n = 4, 1111 까지 모든 수에 대해서 1이 켜졌는지 꺼졌는지, 즉 조합을 구함
# 아무리 커도 2**10
# 시간복잡도는 2**10 * 10 -> 시간 초과 안남
for num in range(1, k+1):
    tmp_a = 1
    tmp_b = 0
    for k in range(10):
        val = 1<<k
        if val > num: break
        if (num & val) != 0:
            tmp_a *= nums[num & val][0]
            tmp_b += nums[num & val][1]
    con = abs(tmp_a-tmp_b)
    if con < min_diff:
        min_diff = con
print(min_diff)    