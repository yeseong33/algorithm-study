# 방문 조건을 리스트에 방문한 곳을 넣고 이곳에 중복 되는지 아닌지 판단
import sys

n, m = map(int, sys.stdin.readline().split())

nums = list(map(int, sys.stdin.readline().split()))

nums.sort()
stack = []


def BT():
    global stack
    
    if len(stack) == m:
        print(*stack)
    
    
    else:
        for i in range(n):
            if nums[i] not in stack:
                stack.append(nums[i])
                BT()
                stack.pop()
BT()


# 방문 조건을 리스트의 인덱스를 사용해 True, False로 만듦
import sys

n, m = map(int, sys.stdin.readline().split())

nums = list(map(int, sys.stdin.readline().split()))

nums.sort()
visited = [False] * n
stack = []

def BT(count):
    
    if count == m:
        print(*stack)

    for i in range(n):
        if visited[i]:
            continue
        visited[i] = True
        stack.append(nums[i])
        BT(count+1)
        visited[i] = False
        stack.pop()
        
BT(0)            


# 두번째 식이 인덱스를 사용해 조건을 확인 하므로 조금 더 빠르다.