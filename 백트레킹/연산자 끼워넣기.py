import sys

n = int(input())
nums = list(map(int, sys.stdin.readline().split()))
oper = list(map(int, sys.stdin.readline().split()))
ans = []
r = []


def d():
    if oper.count(0) == 4:
        r.append(print_ans(ans))
        return
    
    else:
        for i in range(4):
            if oper[i] != 0:
                oper[i] -= 1
                ans.append(str(i+1))
                d()
                oper[i] += 1
                ans.pop()
                
                

def print_ans(x):
    k = nums[0]
    for j in nums[1:]:
        for i in x:
            if i == '1':
                k += j
                x = x[1:]
                break
            elif i == '2':
                k -= j
                x = x[1:]
                break
            elif i == '3':
                k *= j
                x = x[1:]
                break
            elif i == '4':
                if k < 0:
                    k = abs(k)// j
                    k = -k
                    x = x[1:]
                else:
                    k //= j
                    x = x[1:]
                break
    return k
    
    

d()
print(max(r))
print(min(r))