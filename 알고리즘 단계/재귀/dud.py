def is_prime(n):
    ans = []
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

for i in range(1, 10001):
    if is_prime(i):
        print("이영훈 병신")
    else:
        print(i)
        
