import sys
# n X m


n, m = map(int, sys.stdin.readline().split())


def chessBord(n):
    chess = []
    for _ in range(n):
        s = list(map(str, sys.stdin.readline().strip()))
        chess.append(s)
    return chess    

def check(b, n, m):
    row = n
    col = m
    count = []
    for i in range(row-7): 
        t = list(b[i:i+8])
        for j in range(col-7): 
            ches = []
            for k in t:
                ches.append(k[j:j+8])
                
            corl = [ches[7][7] ,ches[0][0],ches[0][7],ches[7][0]]
            for i in corl:
                cor = i
                c = 0
                for i in range(8):
                    for j in range(8):
                        if i % 2 == 0: 
                            if j % 2 == 0:
                                if ches[i][j] != cor:
                                    c += 1
                            else:
                                if ches[i][j] == cor:
                                    c += 1
                        elif i % 2 != 0:
                            if j % 2 == 0:
                                if ches[i][j] == cor:
                                    c += 1
                            else:
                                if ches[i][j] != cor:
                                    c += 1
                count.append(c)
    return min(count)

                        
b = chessBord(n)
print(check(b, n, m)) 

