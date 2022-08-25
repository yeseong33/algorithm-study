s = input()

n = len(s)
n_s = set(s)

ans = []
k = 1

while k <= n:
    if n != 0:
        for i in range(n-k+1):
            ans.append(s[i:i+k])
    k += 1

ans = list(set(ans)) 

print(len(ans))