# import sys
# from heapq import heappop, heappush

# n, m, k = map(int, sys.stdin.readline().split())

# nutri = [[0] * (n+1)]
# total_tree = m
# land = [[[dict(), 5] for i in range(n+1)] for i in range(n+1)]

# for i in range(n):
#     t = [0] + list(map(int, sys.stdin.readline().split()))
#     nutri.append(t)

# for i in range(m):
#     x, y, z = map(int, sys.stdin.readline().split())
#     land[x][y][0][str(z)] = 1

# def solution(land, nutri):
#     d = [(1, 0), (0, 1), (-1, 0), (0, -1), (1, 1), (-1, -1), (1, -1), (-1, 1)]
#     def springAndSummer():
#         global total_tree
#         for i in range(1, n+1):
#             for j in range(1, n+1):
#                 trees = land[i][j][0]
#                 if trees == {}: 
#                     continue
#                 nu = land[i][j][1]
#                 no_nu = False
#                 new_trees = dict()
                
#                 for age in trees:
#                     if no_nu:
#                         total_tree -= trees[age]
#                         nu += (int(age)//2) * trees[age]
#                         continue
#                     total = trees[age] * int(age)
#                     if nu >= total:
#                         new_trees[str(int(age)+1)] = trees[age] 
#                         nu -= total
#                     else:
#                         sup = nu//int(age)
#                         if sup != 0:
#                             new_trees[str(int(age)+1)] = sup
#                             nu -= int(age) * sup 
#                         total_tree -= trees[age] - sup
#                         nu += (int(age)//2) * (trees[age] - sup)
#                         no_nu = True
#                 land[i][j][0] = new_trees
#                 land[i][j][1] = nu
#         return 

#     def fallAndWinter():
#         global total_tree
#         for i in range(1, n+1):
#             for j in range(1, n+1):
#                 trees = land[i][j][0]
#                 land[i][j][1] += nutri[i][j]
#                 for age in trees:
#                     if int(age)%5 == 0:
#                         for t in range(8):
#                             ni = i + d[t][0]
#                             nj = j + d[t][1]

#                             if 0 < ni <= n and 0 < nj <= n:
#                                 total_tree += trees[age]

#                                 if '1' not in land[ni][nj][0]:
#                                     land[ni][nj][0]['1'] = trees[age]
#                                     land[ni][nj][0] = dict(sorted(land[ni][nj][0].items()))
#                                 else:
#                                     land[ni][nj][0]['1'] += trees[age]
#     for pp in range(k):
#         springAndSummer()
#         fallAndWinter()
#     return

# solution(land, nutri)
# print(total_tree)

import sys
from heapq import heappop, heappush

n, m, k = map(int, sys.stdin.readline().split())

nutri = [[0] * (n+1)]
total_tree = m
land = [[[[], 5] for _ in range(n+1)] for _ in range(n+1)]

for i in range(n):
    t = [0] + list(map(int, sys.stdin.readline().split()))
    nutri.append(t)

for i in range(m):
    x, y, z = map(int, sys.stdin.readline().split())
    heappush(land[x][y][0], z)

def solution(land, nutri):
    d = [(1, 0), (0, 1), (-1, 0), (0, -1), (1, 1), (-1, -1), (1, -1), (-1, 1)]
    
    def springAndSummer():
        global total_tree
        for i in range(1, n+1):
            for j in range(1, n+1):
                trees = land[i][j][0]
                trees.sort()
                if trees == []: continue
                nu = land[i][j][1]
                new_trees = []
                dead = 0
                for age in trees:
                    if age <= nu:
                        nu -= age
                        new_trees.append(age+1)
                    else:
                        dead += age//2
                        total_tree -= 1
                nu += dead
                land[i][j][0] = new_trees
                land[i][j][1] = nu
        return 

    def fallAndWinter():
        global total_tree
        for i in range(1, n+1):
            for j in range(1, n+1):
                trees = land[i][j][0]
                land[i][j][1] += nutri[i][j]
                if trees == []: continue
                for age in trees:
                    if age%5 == 0:
                        for t in range(8):
                            ni = i + d[t][0]
                            nj = j + d[t][1]
                            if 0 < ni <= n and 0 < nj <= n:
                                total_tree += 1
                                land[ni][nj][0].append(1)
    for _ in range(k):
        springAndSummer()
        fallAndWinter()

    return

solution(land, nutri)
print(total_tree)