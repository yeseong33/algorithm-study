n = int(input())

while True:
    for i in range(2, n+1):
        if n % i == 0:
            k = i
            break
    if n == 1:
        break
    else:
        n = n // k
        print(k)
        
        
##
n = int(input())
k = 2

# n 값이 1이 되면 멈춤
while n != 1:
    ## 소수값인지를 확인
    if k > n **(0.5):
        print(n)
        exit(0)
        
    # 소인수 분해 가능한 수 일 경우 소인수 분해함
    # 아닐경우 k 값을 1씩 증가시킴 -> 모든 수를 거침
    if n % k == 0:
        print(k)
        n //= k
    else:
        k += 1
        