import sys

n = int(sys.stdin.readline())
nums = sys.stdin.readline().strip()
ans = 0
for i in nums:
    ans += int(i)
print(ans)



input()
print(sum(map(int, input())))
# map 함수는 일반적으로 2번째 매개변수를 첫번째 매개변수에
# 적용시켜준다.
