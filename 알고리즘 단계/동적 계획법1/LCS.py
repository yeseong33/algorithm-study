a = input()
b = input()
a_len = len(a)
b_len = len(b)

big = []
small = []

if a_len > b_len:
    for i in a:
        big.append(i)
    for i in b:
        small.append(i)
else:
    for i in b:
        big.append(i)
    for i in a:
        small.append(i)

c =0 
#    A C A Y K P
# C  0 1 0 0 0 0
# A  1 1 2 0 0 0
# P  1 1 2 0 0 3 
# C  1 2 2 0 0 3
# A  1 2 3 0 0 3 
# K  1 2 3 0 4 3

ans = [0] * len(big)
for i in range(len(small)):
    c = 0
    for j in range(len(big)):
        if c < ans[j]:
            c = ans[j]
        elif small[i] == big[j]:
            ans[j] = c + 1
            

print(max(ans)) 