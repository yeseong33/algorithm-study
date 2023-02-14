import sys

def dfs(stack, n, idx):
    global nums
    
    if len(stack) == 6:
        print(*stack)            
            
    else:
        for i in range(idx, n+1):
            stack.append(nums[i])
            dfs(stack, n, i+1)
            stack.pop()
            
while True:
    nums = list(map(int, sys.stdin.readline().split()))
    
    if nums[0] == 0:
        break
    
    dfs([], nums[0], 1)
    print()
    

