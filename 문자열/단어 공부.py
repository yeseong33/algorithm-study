s = input()
alpa = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
cap = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

a = [0]*26
aidx = 0
q = 0

for i in alpa:
    c = s.count(i)
    idx = alpa.index(i)
    if idx >= 26:
        idx -= 26
    a[idx] += c

m = max(a)
aidx = a.index(m)
if a.count(m) > 1:
    print('?')
else:
    print(alpa[aidx+26])
 
