visited = []
max_k = 0
s = ''
def bt(number, k, idx):
    global max_k, s
    
    if len(s) == len(number) - k:
        tmp = int(s)
        print(visited)
        if tmp > max_k:
            max_k = tmp
        return
    
    
    for i in range(idx, len(number)):
        if i not in visited:
            visited.append(i)
            s += number[i]
            bt(number, k, i+1)
            visited.pop()
            s = s[:len(s)-1]

            


def solution(number, k):
    global max_k
    
    bt(number, k, 0)
    print(max_k)
    
    answer = ''
    return answer

solution("1231234", 3)