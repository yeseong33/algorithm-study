import sys
import cProfile

def so():
    import sys
    while True:
        ns = [1, 10, 13, 100, 1000, 10000, 100000, 0]
        for n in ns:
            if n == 0:
                break
            nums = [True for i in range(2*n+1)]
            for i in range(2, int((2*n) ** 0.5)+1):
                if nums[i]:
                    for i in range(i*i, 2*n+1, i):
                                ## i * i로 해주는 이유
                                ## i+i 로 하면 2i 가 되며 이후에 계속 i 가 더해지는 식인데
                                ## 짝수인 것에 대해서는 i 가 2일 때 모두 처리 되므로
                                # 그 스스로의 배수들에 대해서만 체크해주기 위해 
                                # i * i 를 사용한다. 

                        nums[i] = False
            print(nums[n+1:2*n+1].count(True))
        if n == 0:
                break


import cProfile

cProfile.run("so()")




#######
def get_prime_array(N: int):
    # N보다 작은 소수를 모두 출력
    
    if N < 2:
        return []
    N = N+1
    Sieve = [1] * (N // 2) #홀수에 대해서만 Sieve를 구성해서 탐색 범위 감소
    for i in range(3, int(N ** 0.5)+1, 2): #3부터 시작되는 홀수에 대해서만 대응 N의 소수는 Root(N+1)보다 클 수 없음
        if Sieve[i // 2] == 1:
            k = i * i
            #Sieve[k//2 : : i] = [0] * ((N-k-1) // (2*i) +1)
            for j in range(k//2, N//2 , i):
                Sieve[j] = 0
    return Sieve
    
def get_prime_number(A):
    # get_prime_array 필요
    # 정수를 입력 받으면 해당 정수 보다 작은 소수를 출력

    if (type(A) == int):
        A = get_prime_array(A)
    
    ans = [2]
    for i in range(1, len(A)):
        if A[i] == 1:
            ans.append(2*i+1)
    return ans

    # return [2] + [(2 * i + 1) for i in range(1, n // 2) if save[i]]

def Search(prime, n):
    l,r = 0, len(prime)-1
    while l<=r:
        m=(l+r)//2

        if prime[m] > n:
            r = m-1
        else:
            l = m+1
    return l

import sys
S = get_prime_number(123456*2)
while(1):
    N = int(sys.stdin.readline())
    if N ==0:
        break
    print(Search(S,2*N) - Search(S,N))