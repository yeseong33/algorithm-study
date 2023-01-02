def fac(n):
    k = 1
    for i in range(1, n+1):
        k *= i
    return k


n = int(input())
s = str(fac(n))
c = 0

while s[-1] == '0':
    c += 1
    s = s[:-1]

print(c)

