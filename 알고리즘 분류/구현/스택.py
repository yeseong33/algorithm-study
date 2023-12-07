import sys
n = int(input())

stack = []
for i in range(n): 
    string = list(sys.stdin.readline().split())
    code = string[0]
    num = string[-1]
    
    if code == 'push':
        stack.append(num)
    elif code == 'pop':
        if not len(stack):
            print(-1)
        else:
            print(stack.pop())
    elif code == 'size':
        print(len(stack))
    elif code == 'empty':
        print(0 if len(stack) else 1)
    else:
        print(-1 if not len(stack) else stack[-1])
        
        