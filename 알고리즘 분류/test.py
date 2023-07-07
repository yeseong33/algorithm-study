n = 0
k = []
visited = [0] *n
pa = []
ans = []

def solution(S):
    global n, k, visited, pa, ans
    nums = list(S)
    n = len(nums)
    visited = [0] *n
    dfs(S)
    if ans == []:
        ttt = '0'
    else:
        ttt = str(max(ans))
    return ttt

def isP(s):
    mi = len(s)
    if mi % 2 == 0:
        a_h = s[:mi//2]
        a_t = s[mi//2:]
        a_t.reverse()
        if a_h == a_t:
            return True
    else:
        a_h = s[:mi//2]
        m = s[mi//2]
        a_t = s[mi//2+1:]
        a_t.reverse()
        if a_h == a_t:
            return True
    return False

def dfs(ss):

    if len(k) > n:
        return
    else:
        if isP(k):
            s = ''
            count = 0
            for i in k:
                if s == '' and i == '0':
                    count += 1
                    continue
                else:
                    s += i
            s_len = len(s)                
            s = s[:s_len-count]
            if s != '':
                ans.append(int(s))

    for i in range(n):
        if not visited[i]:
            k.append(ss[i])
            visited[i] = 1
            dfs(ss)
            visited[i] = 0
            k.pop()

s = solution('0103112')
print(s)