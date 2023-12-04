MAX_N = 10000

Num = [0 for _ in range(MAX_N)]
Child = [[0, 0] for _ in range(MAX_N)]
Parent = [0 for _ in range(MAX_N)]
Root = 0
Limit = 0
Cnt = 0
def dfs(node):
    global Cnt
    if node == -1:
        return 0
    
    if Num[node] > Limit:
        Cnt = MAX_N +1
        return Num[node]
        
    numL = dfs(Child[node][0])
    numR = dfs(Child[node][1])

    if numL + numR + Num[node] <= Limit:
        return numL + numR + Num[node]
    if numL == 0 or numR == 0:
        Cnt += 1
        return Num[node]
    
    if numL + Num[node] <= Limit and numR + Num[node] <= Limit:
        Cnt += 1
        return numL + Num[node] if numL < numR else numR + Num[node]
    
    if numL + Num[node] <= Limit:
        Cnt += 1
        return numL + Num[node]
    if numR + Num[node] <= Limit:
        Cnt += 1
        return numR + Num[node]
    Cnt += 2
    return Num[node]
    

def check(limit, k):
    global Cnt, Limit
    Cnt = 0
    Limit = limit
    dfs(Root)
    if Cnt < k:
        return True
    return False


def solution(k, num, links):
    global Root
    
    sum = 0
    for i in range(len(num)):
        Parent[i] = -1
        Num[i] = num[i]
        sum += num[i]
    for i in range(len(num)):
        Child[i][0] = links[i][0]
        if Child[i][0] != -1:
            Parent[Child[i][0]] = i
        Child[i][1] = links[i][1]
        if Child[i][1] != -1:
            Parent[Child[i][1]] = i
            
    for i in range(len(num)):
        if Parent[i] == -1:
            Root = i
            break
    
    low = sum//k
    high = sum
    while low <= high:
        mid = (low+high)//2
        if check(mid, k):
            high = mid-1
        else:
            low = mid+1
        
    answer = 0
    return answer