# 움직임 구현

import sys

gear = []

for i in range(4):
    
    tt = list(map(int, sys.stdin.readline().strip()))
    gear.append(tt)

k = int(input())

m = []
for i in range(k):
    tt = list(map(int, sys.stdin.readline().split()))
    m.append(tt)

# 2, 6
# n = 0, s = 1
def move(g_num, w, moved):
    moved[g_num] = 1
    
    now_two = gear[g_num][2]
    now_six = gear[g_num][6]
    
    left = g_num - 1
    right = g_num + 1
    
    if left != -1:
        next_left_two = gear[left][2]
        if now_six != next_left_two: 
            if moved[left] == 0:
                move(left, -w, moved)
            
    if right != 4:
        next_right_six = gear[right][6]
        if now_two != next_right_six:
            if moved[right] == 0: 
                move(right, -w, moved)
    
    
    if w == -1:
        first = gear[g_num][0] 
        for i in range(7):
            gear[g_num][i] = gear[g_num][i+1]
        gear[g_num][7] = first
    else:
        end = gear[g_num][-1]
        for i in range(7, 0, -1):
            gear[g_num][i] = gear[g_num][i-1]
        gear[g_num][0] = end
    
    
def check():
    score = 0
    for i in range(4):
        if gear[i][0] == 1:
            score += 2 **(i)
    return score
            


def Gear():
    
    for i in range(k):
        moved = [0, 0, 0, 0]

        gear_num = m[i][0] -1 
        way = m[i][1]
        
        move(gear_num, way, moved)
        

    s = check()
    print(s)
        
Gear()