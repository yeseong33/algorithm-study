import sys

s = list(sys.stdin.readline().strip())


in_bracket = ['(', '[']
out_bracket = [')',']']

stack = []

nums = [-1] * 1000
ans = 0
pas = False
for i in range(len(s)):
    
    now = s[i]
    
    if now in in_bracket:
        stack.append(now)
    elif now in out_bracket and len(stack) != 0:
        tmp = stack.pop()
        tmp_idx = len(stack)
        if stack != []:
            if in_bracket.index(tmp) == out_bracket.index(now):
                mode = 0
                if now == ')':
                    mode = 2
                else:
                    mode = 3
                    
                a = 0
                if nums[tmp_idx] == -1:
                    a = mode
                else:
                    a = mode * nums[tmp_idx]
                    nums[tmp_idx] = -1
                    
                if nums[tmp_idx-1] == -1:
                    nums[tmp_idx-1] = a
                else:
                    nums[tmp_idx-1] += a
            else:
                pas = True
                break
        else:
            if in_bracket.index(tmp) == out_bracket.index(now):
                k = 0
                if now == ')':
                    k = 2
                else:
                    k = 3
                if nums[tmp_idx] == -1:
                    ans += k
                else:
                    ans += k * nums[tmp_idx]
                    nums[tmp_idx] = -1
            else:
                pas = True
                break
    else:
        pas = True
        break
            
    
if stack != [] or pas:
    print(0)
else:
    print(ans)
    