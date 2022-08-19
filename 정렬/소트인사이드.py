num = list(input())
num.sort(reverse=True)

s = ''
for i in range(len(num)):
    s += num[i]
print(s)

