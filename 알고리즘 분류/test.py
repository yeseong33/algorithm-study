
ans = 4

li1 = [3,2, 1]
li2 = []
li3 = []
t = [[], [], []]
count =1 

def move(n, start, to):
    global count
    count += 1
    
    k = start.pop()
    to.append(k)
    
    if count == ans:
        t[0] = li1.copy()
        t[1] = li2.copy()
        t[2] = li3.copy()


def com(n, start, to, tmp):
    global count
    if n == 1:
        move(1, start, to)
    else:
        com(n-1, start, tmp, to)
        move(n, start, to)
        com(n-1, tmp, to, start)

com(3, li1, li3, li2)

def draw(t):
    drv = '    [DRV]'
    dis = '+-------+|       ||DISPLAY||       |+-------+'
    compute = '+-------+|COMPUTE|+-------+'
    plus = '1========|2========|3========|'
    
    
    h = 1
    e_h = [1,1, 1]
    for i in range(3):
        for j in t[i]:
            if j == 1:
                h += 1
                e_h[i] += 1
            elif j == 2:
                h += 5
                e_h[i] += 5
            elif j == 3:
                h += 3
                e_h[i] += 3
                
    s = [[' '] * 30 for _ in range(h-1)]
    s.append(list(plus))
    print(t)
    print(h)
    for i in range(3):
        tmp_h = h
        for yt in t[i]:
            if yt == 1:
                for x in range(tmp_h-2, tmp_h-2-1, -1):
                    print(i, tmp_h, 'ff')
                    for y in range(i *10, i*10 + 9):
                        s[x][y] = drv[0]
                        drv = drv[1:]
                tmp_h -= 1
            elif yt == 2:
                for x in range(tmp_h-2, tmp_h-2-5, -1):
                    for y in range(i *10, i*10 + 9):
                        s[x][y] = dis[0]
                        dis = dis[1:]
                tmp_h -= 5
            elif yt == 3:
                for x in range(tmp_h-2, tmp_h-2-3, -1):
                    for y in range(i *10, i*10 + 9):
                        s[x][y] = compute[0]
                        compute = compute[1:]
                tmp_h -= 3
                
    
    for i in s:
        print(''.join(i))

draw(t)
