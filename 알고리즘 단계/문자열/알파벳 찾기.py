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
# find �Լ�: string �ȿ��� ã���� �ϴ� �Ű������� 
# �ε��� ���� ����ش�.
