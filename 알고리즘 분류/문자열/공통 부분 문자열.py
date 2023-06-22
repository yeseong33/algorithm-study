import sys

A = sys.stdin.readline().strip()
B = sys.stdin.readline().strip()


start = 0
end = 1
max_len = 0
pas = False

while end < len(A)+1:
    s_a = A[start:end]
    # print(s_a, 'a')
    s = 0
    e = end-start
    while e < len(B)+1:
        s_b = B[s:e]
        # print(s_b, 'b')
        if s_a == s_b:
            if max_len < e-s:
                max_len = e-s
                # print(s_a, 'max')
            pas = True
            break
        s += 1
        e += 1
        
    if pas:
        end += 1
        # print(end)
        pas = False
    else:
        if end-start > 1:
            if max_len == 0:
                start += 1
            else:
                start += 1
                end = start + max_len
        else:
            end += 1
            start += 1

print(max_len)
# asdf
# asdf