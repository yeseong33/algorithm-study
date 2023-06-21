import sys

n ,m = map(int, sys.stdin.readline().split())


room = []

for i in range(n):
    k = list(map(int, sys.stdin.readline().split()))
    room.append(k)

cctv = []
tt = 0


for i in range(n):
    for j in range(m):
        if room[i][j] != 0 and room[i][j] != 6:
            cctv.append([i, j])
        if room[i][j] != 0:
            tt += 1

d = [(-1, 0), (0, -1), (1, 0), (0, 1)]  
max_count = 0
def bt(room, cctv, idx):
    global max_count
    
    if idx == len(cctv):
        c = count_s(room)
        if c > max_count:
            max_count = c
        
        return
    
    tmp = deep_copy(room)

    x, y = cctv[idx]
    if room[x][y] == 1:
        for j in range(4):
            tmp = fill(tmp, [j], x, y)
            bt(tmp, cctv, idx + 1)
            # room = remove(room, [j], x, y)
            tmp = deep_copy(room)
    elif room[x][y] == 2:
        for j in range(2):
            tmp = fill(tmp, [j, j+2], x, y)
            bt(tmp, cctv, idx+1)
            # room = remove(room, [j, j+2], x, y)
            tmp = deep_copy(room)
            
    elif room[x][y] == 3:
        for j in range(4):
            tmp = fill(tmp, [j, (j+1)%4], x, y)
            bt(tmp, cctv, idx + 1)
            # room = remove(room, [j,(j+1)%4], x, y)
            tmp = deep_copy(room)

    elif room[x][y] == 4:
        for j in range(4):
            tmp = fill(tmp, [j, (j+1)%4, (j+2)%4], x, y)
            bt(tmp, cctv, idx + 1)
            # room = remove(room, [j,(j+1)%4, (j+2)%4], x, y)       
            tmp = deep_copy(room)

    else:
        tmp = fill(tmp, [0, 1, 2, 3], x, y)
        bt(tmp, cctv, idx + 1)
        # room = remove(room, [0, 1, 2, 3], x, y)   
        tmp = deep_copy(room)




def fill(r, dir, x, y):
    
    for i in dir:
        nx = x + d[i][0]
        ny = y + d[i][1]
        while 0 <= nx <= n-1 and 0 <= ny <= m-1:
            if r[nx][ny] == 6:
                break
            elif r[nx][ny] == "#":
                r[nx][ny] = '##'
            elif r[nx][ny] == 0:
                r[nx][ny] = '#'
            nx = nx + d[i][0]
            ny = ny + d[i][1]
    return r
    
# def remove(r, dir, x, y):
    
#     for i in dir:
#         nx = x + d[i][0]
#         ny = y + d[i][1]
        
#         while 0 <= nx <= n-1 and 0 <= ny <= m-1:
#             if r[nx][ny] == '##':
#                 r[nx][ny] = '#'
            
#             elif r[nx][ny] == '#':
#                 r[nx][ny] = 0
            
#             elif r[nx][ny] == 6:
#                 break
#             nx = nx + d[i][0]
#             ny = ny + d[i][1]
#     return r
def deep_copy(a):
    k = [item[:] for item in a]
    return k 

def count_s(r):
    c = 0 
    
    for i in range(n):
        for j in range(m):
            if r[i][j] == '#' or r[i][j] == '##':
                c += 1
    return c


bt(room, cctv, 0)

print(m*n - max_count- tt)

