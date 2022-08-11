cro = ['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z=']

s = input()
count = 0
strlen = len(s)

for i in cro:
    if i in s:
        c = s.count(i)
        iLen = len(i)
        
        if i == 'z=' and c >= 2 and 'dz=' in s:
            c -= s.count('dz=')
        elif i == 'z=' and  s.count('z=') == s.count('dz='):
            continue
        
        count += 1 * c
        strlen -= iLen * c
count += strlen 
print(count)



## 
# s = input()
