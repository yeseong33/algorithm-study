# # -가 나타나면 괄호 시작 
# # 다시 -가 나타가거나 끝나기 전에 괄호를 닫음
# import sys


s = input()
idx = s.find('-')

if idx != -1:
    plus = s[:idx]
    mius = s[idx+1:] 
       
        
    mius = mius.replace('-', '+')
    

    p_nums = list(map(int, plus.split('+')))
    m_nums = list(map(int, mius.split('+')))
    total = sum(p_nums) - sum(m_nums)
    print(total)
else:
    p_nums = list(map(int,s.split("+")))
    print(sum(p_nums))

