n = int(input())
fib_c = 0
fibonacci_c = 0
f = [1, 1] + [0] * (n-2)
k = [1, 1] + [0] * (n-2)


def fib(n):
    global fib_c
    
    for i in range(2, n):
        k[i] = k[i-1] + k[i-2]
        fib_c += 1
    
    return k[-1]
    

def fibonacci(n):
    global fibonacci_c
    
    for i in range(2, n):
        f[i] = f[i-1] + f[i-2]
        fibonacci_c += 1
    
    return f[-1]


fibonacci(n)
print(fib(n), end =' ')
print(fibonacci_c)        