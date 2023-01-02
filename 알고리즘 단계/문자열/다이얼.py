alp = ['ABC', 'DEF', 'GHI', 'JKL', 'MNO', 'PQRS', 'TUV', 'WXYZ']

s = list(map(str, input()))
time = 0
for i in s:
    for j in alp:
        if i in j:
            num = alp.index(j)+2
    time += num+1
print(time)


    