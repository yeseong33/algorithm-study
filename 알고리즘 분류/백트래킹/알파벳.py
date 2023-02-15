import sys

r, c = map(int, sys.stdin.readline().split())

map = []
move = 0 
D = [(1, 0), (-1, 0), (0, 1), (0, - 1)]

for i in range(r):
    k = input()
    t = []
    for j in k:
        t.append(j)
    map.append(t)
    
visited = [[False] * c for _ in range(r)]

track = [False] * 26
track[ord(map[0][0])-65] =True



def BT(i,j, total):
    global move, D

    # 종료 조건
    if move < total:
        move = total
    
    # 유망한 것 거르기 및 재귀
    for k in range(4):
        ni = i + D[k][0]
        nj = j + D[k][1]
        
        if ni < 0 or ni >= r or nj < 0 or nj >= c:
            continue
        al = ord(map[ni][nj]) - 65
        
        if not track[al]:
            visited[ni][nj] = True 
            track[al] =  True
            total += 1
            BT(ni, nj, total)
            visited[ni][nj] = False
            track[al] = False
            total -= 1
            


BT(0, 0, 1)
print(move)

