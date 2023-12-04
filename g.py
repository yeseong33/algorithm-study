from bisect import bisect_left

def solution(info, query):
    wmap = {'-':0, 'cpp': 1, 'java':2, 'python':3,
            'backend': 1, 'frontend': 2, 
            'junior': 1, 'senior': 2,
            'chicken':1, 'pizza': 2}
    
    slist = [[] for i in range(4*3*3*3)]
    
    for string in info:
        w = string.split()
        arr = (wmap[w[0]] * 3*3*3,
               wmap[w[1]] * 3*3,
               wmap[w[2]] * 3,
               wmap[w[3]])
        score = int(w[4])
        
        for i in range(1<<4):
            idx = 0
            for j in range(4):
                if i & (1<<j):
                    idx += arr[j]
            slist[idx].append(score)

    for i in range(4*3*3*3):
        slist[i] = sorted(slist[i])
    ans = []
    for string in query:
        w = string.split()
        idx = wmap[w[0]]*3*3*3+wmap[w[2]]*3*3+wmap[w[4]]*3+wmap[w[6]]
        score = int(w[7])
        ans.append(len(slist[idx]) - bisect_left(slist[idx], score))
    return ans
            
solution(["java backend junior pizza 150","python frontend senior chicken 210","python frontend senior chicken 150","cpp backend senior pizza 260","java backend junior chicken 80","python backend senior chicken 50"], ["java and backend and junior and pizza 100","python and frontend and senior and chicken 200","cpp and - and senior and pizza 250","- and backend and senior and - 150","- and - and - and chicken 100","- and - and - and - 150"])