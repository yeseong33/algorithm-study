# 1. 빈 스택 두개 만듬
# 2. 하나는 수열로 만들어 진 것
# 3. 하나는 빈 스택
# 4. push pop 을 반복하면서 가능한 것인지 확인

# deque를 이용한 풀이
import sys
from collections import deque

ans = deque()
stack = deque()
result = []

n = int(input())
flag = 1
num = 1
count = 0

for _ in range(n):
    k = int(sys.stdin.readline())
    ans.append(k)
    

while count != 2 * n:
    if flag != 0:
        pop = ans.popleft()
        flag = 0
    
    
    if len(stack) == 0 or stack[0] != pop:
        stack.appendleft(num)
        num += 1
        result.append('+')    
    elif pop == stack[0]:
        result.append('-')
        stack.popleft()
        flag = 1
        
    count += 1 
    

if result.count('+') == result.count('-'):
    for i in result:
        print(i)
else:
    print("NO")

# # 1. ans.pop() 을 통해 정해진 수열에서 맨 앞자리 뽑아옴        
# # 2. 만약 stack 이 비어 있거나 맨 앞의 값이 pop 과 같지 않을경우 --> 다음 오름차순을 push
# # 3. 만약 pop 과 stack의 맨 앞 값이 같으면 --> stack에서 pop 하는 것으로 표현  
# # 4. 이를 반복하다가 n*2 즉, 수열을 만들 수 있을 경우에 +, -합이 2n 이 되어야 함
# # 5. 이를 검사 + 개수와 - 개수가 같을 경우 --> 수열을 만들 수 있음
# # 아닐 경우 --> 수열을 만들 수 없음

# # deque 라이브러리를 익숙하게 사용하지 못함
# # 리스트를 사용하면 더 빠르게 풀 수 있었을 것


# 리스트를 이용한 풀이
import sys

n = int(input())

nums = []
stack = []
ans = []

num = 1
count = 0

for _ in range(n):
    nums.append(int(sys.stdin.readline()))

nums.reverse()

while count != 2*n:
    pop = nums[-1]
    
    if stack == [] or stack[-1] != pop:
        stack.append(num)
        ans.append('+')
        num += 1
    elif pop  == stack[-1]:
        stack.pop()
        ans.append('-')
        nums.pop()
    
    count += 1
    
if ans.count('+') == ans.count('-'):
    for i in ans:
        print(i)
else:
    print("NO")