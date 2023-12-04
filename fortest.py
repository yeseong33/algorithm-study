from itertools import combinations
from itertools import product

def solution(dice):
    real_ans = []
    n = len(dice)
    k = set()
    d = [i for i in range(n)]
    combi = list(combinations(d, n//2))
    dmap = dict()
    dmap_idx = []
    for i in combi:
        if list(i) in dmap.values():
            continue
        v = [0] * n
        tmp = []
        for j in i:
            v[j] =  1
        for idx, j in enumerate(v) :
            if j == 0:
               tmp.append(idx)
        dmap[list(i)] = tmp
        dmap_idx.append(i) 
        
    def make(a):
        i = a
        tmp = []
        ans_1 = []
        for j in i:
            tmp.append(dice[j])
        combi_sum = list(product(*tmp)) 
        l = len(combi_sum)
        for v in range(l):
            ans_1.append(sum(combi_sum[v]))
        print(ans_1)
        i = dmap[a]
        tmp = []
        ans_2 = []
        for j in i:
            tmp.append(dice[j])
        combi_sum = list(product(*tmp)) 
        l = len(combi_sum)
        for v in range(l):
            ans_2.append(sum(combi_sum[v]))
        print(ans_2)
        return ans_1, ans_2
    for i in dmap:
        a, b =make(i)
        combi_m = list(product(a, b)) 
        l = len(combi_m)
        print(l)
        k = [0] * l
        k_2 = [0] *l
        for v in range(l):
            if combi_m[v][0] > combi_m[v][1]:
                k[v] += 1
            elif combi_m[v][0] < combi_m[v][1]:
                k_2[v] += 1
        real_ans.append(k.count(1))
        real_ans.append(k_2.count(1))
    print(real_ans)
    ids = real_ans.index(max(real_ans))
    if ids%2 == 0:
        ids = ids//2
        valu = dmap_idx[ids]
        valu = list(valu)
        valu[0] += 1
        valu[1] += 1
    else:
        ids = ids//2
        print(dmap_idx)
        valu = dmap_idx[ids]
        # print(valu)
        # valu = dmap[valu]
        # valu = list(valu)
        # print(valu)
        # valu[0] += 1
        # valu[1] += 1

    
    answer = valu
    print(answer, 'ekq')
    return answer

solution([[1, 2, 3, 4, 5, 6], [2, 2, 4, 4, 6, 6]])