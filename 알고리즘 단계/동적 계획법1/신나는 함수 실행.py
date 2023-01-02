def w(a, b, c):
    while True:
        if a <= 0 or b <= 0 or c <= 0:
            return 1
        elif a > 20 or b > 20 or c > 20:
            a, b ,c = 20, 20, 20
        elif a < b < c:
            c -= 1
            
            a_1 = a
            b_1 = b-1
            c_1 = c-1
            
            a_2 = a
            b_2 = b-1
            c_2 = c
            
            
        else:
            w(a-1, b, c) + w(a-1, b-1, c) + w(a-1, b, c-1) - w(a-1, b-1, c-1)
        

print(w(1, 2, -1))


## 다시 풀기