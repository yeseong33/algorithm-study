s = input()

minus = False
nums = list()
temp = s[:]
t_nums = 0
idx = 0 
ans = 0

for i in range(len(s)):
    if s[i] == '-':
        nums.append(temp[idx:i])
        nums.append('-')
        idx = i+1
    elif s[i] == '+':
        nums.append(temp[idx:i])
        nums.append('+')
        idx = i+1
    if i == len(s)-1:
        nums.append(temp[idx:])


for i in nums:
    if i != '-' and i != '+':
        if minus == False:
            ans += int(i)
        else:
            t_nums += int(i)
    elif i == '-':
        if minus == False:
            minus = True
        else:
            ans -= t_nums
            t_nums = 0
    if i == nums[-1]:
        if minus == True:
            ans -= t_nums

    print(ans)
print(nums)
print(ans)
            
        

