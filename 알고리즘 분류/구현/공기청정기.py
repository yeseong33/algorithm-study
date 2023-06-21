import sys

r, c, t = map(int, sys.stdin.readline().split())


room = []

for i in range(r):
    k = list(map(int, sys.stdin.readline().split()))
    room.append(k)


def takeTime():
        global room
        # 확산과정
        # 어느 공간에 있는지 확인
        micro, airc = checkMiro(room)
        head = airc[0]
        tail = airc[1]
        
        # 그공간을 기준으로 BFS
        d = [(0, 1), (0, -1), (1, 0), (-1, 0)] 
        tmp = [item[:] for item in room]
        while micro:
            a, b = micro.pop()
            move_micro = 0
            
            for i in range(4):
                na = a + d[i][0]
                nb = b + d[i][1]
                
                if 0 <= na <= r-1 and 0 <= nb <= c-1:
                    if room[na][nb] != -1:
                        tmp[na][nb] += room[a][b]//5
                        move_micro += 1
            # 움직이고 나서 현재 위치의 먼지 양
            tmp[a][b] -= (room[a][b]//5) * move_micro
        

        room = [item[:] for item in tmp]
        # 순환과정
        # 머리 순환
        s_s = [(0, 1), (-1, 0), (0, -1), (1, 0)]
        tmp = 0
        x = head[0]
        y = head[1]+1
        i = 0 
        while x != head[0] or y != head[1]:
            
            room[x][y], tmp = tmp, room[x][y]
            
            nx = x + s_s[i][0]
            ny = y + s_s[i][1]
            if ny > c-1:
                i += 1 
                x, y = x-1, y
            elif nx < 0:
                i += 1
                x, y = x, y-1
            elif ny < 0:
                i += 1
                x, y = x+1, y
            else:
                x, y = nx, ny
        # 꼬리 순환
        s_s = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        tmp = 0
        x = tail[0]
        y = tail[1]+1
        i = 0 
        while x != tail[0] or y != tail[1]:
            
            room[x][y], tmp = tmp, room[x][y]
            
            nx = x + s_s[i][0]
            ny = y + s_s[i][1]
            
            if ny > c -1 :
                i += 1 
                x, y = x+1, y
            elif nx > r-1:
                i += 1
                x, y = x, y-1
            elif ny < 0:
                i += 1
                x, y = x-1, y
            else:
                x, y = nx, ny
        


def checkMiro(room_in):
    ans = []
    airc = []
    for i in range(r):
        for j in range(c):
            if room_in[i][j] > 0:
                ans.append([i, j])

            
            if room_in[i][j] == -1:
                airc.append([i, j])        
            
    return ans, airc

# print()
# for i in room:
#     print(*i)
# print()
# takeTime()
# for i in room:
#     print(*i)

for _ in range(t):
    takeTime()

total = 0
for i in range(r):
    for j in range(c):
        if room[i][j] > 0:
            total += room[i][j]
print( total)
# for i in range(t):
#     takeTime()