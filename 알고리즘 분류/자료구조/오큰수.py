# 리스트에 수열 저장, 리스트를 스택으로 이용하기 위해 reverse --> 왼큰수로 생각
# pop을 하고 그 수와 이후의 수들과 비교 만약 큰 순간 ans에 저장
# 다 돌고도 없으면 -1
# ans 출력
# while 안에 for 루프로 검사할 것 --> 시간 복잡도가 되려나?(n = 10 ** 6)

import sys

n = int(input())

nums = list(map(int, sys.stdin.readline().split()))
nums.reverse()
ans = []
b = 0

while nums != []:
    pop = nums.pop()
    
    for i in range(len(nums)-1, -1, -1):
        oks = nums[i]
        if oks > pop:
            ans.append(oks)
            b = 1
            break
    if  b == 0:
        ans.append(-1)
        
    b = 0
for i in ans:
    print(i, end = ' ')

# --> 답은 출력 되나 n이 커서 예상대로 시간초과가 남
# 스택 자료 구조를 잘 이용하지 않아서 발생한 문제로 보임
# 하나하나 비교하기 보다는 pop을 하면서 
# pop 을 하면서 가장 큰 수와 그 다음으로 큰 수를 저장 한다. 
# 이를 pop 한 수와 비교해 가장 오른쪽의 큰수를 구한다. 

import sys

n = int(input())

nums = list(map(int, sys.stdin.readline().split()))


first = nums.pop()
second = -2
min = first
s = '-1'
for _ in range(n-1):
    pop = nums.pop()
    
    if pop < min:
        s = str(min) + ' ' + s
        min = pop    
    elif pop < second:
        s = str(second) + ' ' + s
        # ans.append(second)
    elif pop < first:
        # ans.append(first)
        s = str(first) + ' ' + s
        second = pop
    else:
        s = '-1 ' + s
        first, second = pop, first

print(s)
# -_>오답
# 길이가 길어질 수록 저장해야 하는 값들이 많아짐
# 다른 방향으로 stack 사용



import sys

n = int(input())

nums = list(map(int, sys.stdin.readline().split()))
nums_c = nums.copy()
stack = []
i = 0

for i in range(n):

    while stack and nums[stack[-1]] < nums[i]:
        nums_c[stack.pop()] = nums[i]
    stack.append(i)



for i in range(n):
    if nums[i] == nums_c[i]:
        print('-1', end = ' ')
    else:
        print(nums_c[i], end = ' ')

# --> 정답
# stack을 이용할 때 리스트의 인덱스를 저장하는 방식으로 풀이
