import sys

def solusion(n, numbers):
    

    for i in range(n):
        now = numbers[i]
        now_len = len(now)
        for j in range(i+1, n):
            if now == numbers[j][:now_len]:
                print("NO")
                return 
    
    print("YES")
    return True



t = int(input())

for i in range(t):
    n = int(sys.stdin.readline().strip())
    numbers = []
    for j in range(n):
        k = sys.stdin.readline().strip()
        numbers.append(k)
    numbers.sort()
    
    solusion(n, numbers)
    


        