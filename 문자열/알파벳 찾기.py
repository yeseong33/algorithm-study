s = input()

for i in range(97, 123):
    if chr(i) in s:
        print(s.index(chr(i)), end = ' ')
    elif i == 123:
        print(-1, end = '')
    else:
        print(-1, end = ' ')


##
s = '123'
print(s.find('3'))
# find 함수: string 안에서 찾고자 하는 매개변수의 
# 인덱스 값을 찍어준다.
