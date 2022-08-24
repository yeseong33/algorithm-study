s = input()
n = len(s)
n_s = set(s)
print(n_s)
a = ''
ans = []
k = 1
print(s[0:1])
while k <= n:
    if n != 0:
        for i in range(n-k+1):
            ans.append(s[i:i+k])
    k += 1
ans = list(set(ans)) 

print(ans)
print(len(ans))