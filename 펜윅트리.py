import sys

n, m, k = map(int, sys.stdin.readline())

arr = [0] * (n+1)
tree = [0] * (n+1)


# i번째 수까지 누적합을 계산하는 함수
def prefix_sum(i):
    result = 0
    while i > 0:
        result += tree[i]
        i -= (i&-i)
    return result
# i번째 수를 dif 만큼 더하는 함수
def update(i, dif):
    while i <= n:
        tree[i] += dif
        i += (i&-i)

# start부터 end 까지의 구간 합을 계산하는 함수
def interval_sum(start, end):
    return prefix_sum(end) - prefix_sum(start-1)

for i in range(1, n+1):
    x = int(input())
    arr[i] = x
    update(i, x)


for i in range(m+k):
    a, b, c = map(int, sys.stdin.readline( ))
    # update 연산인 경우
    if a == 1:
        update(b, c-arr[b])
        arr[b] = c
    else:
        interval_sum(b, c)
