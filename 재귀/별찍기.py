import math


def space(s):
    k = math.ceil(math.log(len(s), 3))
    
    for i in range(3 **(k-1), 2 * 3 **(k-1)):
        for j in range(3 **(k-1), 2 * 3 **(k-1)):
            s[i][j] = ' ' 
    return s


def star(n):
    basic = [list(map(str,"***")) for i in range(3)]
    basic = space(basic)
    
    k = math.ceil(math.log(n, 3))


    for i in range(1, k):
        for j in range(len(basic)):
            basic[j] = basic[j] * 3
    
   
        s = []
        for j in range(3**(i+1)):
            j = j % 3**i
            s.append(list(basic[j]))
            
        basic = space(s)

    return basic


def show(s, n):
    for i in range(n):
        for j in range(n):
            print(s[i][j], end = '')
        print('')


n = int(input())

s = star(n)
show(s, n)


###

# s = math.log(243,3)
# print(s)