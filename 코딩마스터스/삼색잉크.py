total = [35, 163, 155, 54, 36, 36, 36, 36, 36, 35]
month = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
day = {'SUN':1, 'MON':7, 'TUE':6, 'WED': 5, 'THU': 4, 'FRI':3, 'SAT': 2 }
day_s = {'SUN':7, 'MON':6, 'TUE':5, 'WED': 4, 'THU': 3, 'FRI':2, 'SAT': 1 }

import sys

s = input()

today_sun = day[s]
today_sat = day_s[s]
n = int(input())
holi = [[] for i in range(12)]
for i in range(n):
    a, b = map(int, sys.stdin.readline().split())
    holi[a-1].append(b)
    
def count_color(today, blue = False):
    i = 0
    month_last = month[i]
    today = today
    color = [0] * 10
    
    if not blue:
        while i != 12:
            if today in holi[i]:
                holi[i].remove(today)
            
            if today // 10 >= 1:
                a = today//10
                b = today%10
                color[a] += 1
                color[b] += 1
            else:
                color[today] += 1
                
            today += 7
            if today > month_last:
                today -= month_last
                i += 1 
                if i < 12:
                    month_last = month[i]
            elif  today >= month_last and i == 11:
                if today == month_last:
                    if today in holi[i]:
                        holi[i].remove(today)
                    if today // 10 >= 1:
                        a = today//10
                        b = today%10
                        color[a] += 1
                        color[b] += 1
                    else:
                        color[today] += 1
                i += 1
                
        return color
    else:
        color_r = [0] * 10
        while i != 12:
            if today in holi[i]:
                holi[i].remove(today)
                if today // 10 >= 1:
                    a = today//10
                    b = today%10
                    color_r[a] += 1
                    color_r[b] += 1
                else:
                    color_r[today] += 1
            else:
                if today // 10 >= 1:
                    a = today//10
                    b = today%10
                    color[a] += 1
                    color[b] += 1
                else:
                    color[today] += 1
            today += 7
            if today > month_last:
                today -= month_last
                i += 1 
                if i < 12:
                    month_last = month[i]
            elif  today >= month_last and i == 11:
                if today == month_last:
                    if today in holi[i]:
                        holi[i].remove(today)
                        if today // 10 >= 1:
                            a = today//10
                            b = today%10
                            color_r[a] += 1
                            color_r[b] += 1
                        else:
                            color_r[today] += 1
                    else:
                        if today // 10 >= 1:
                            a = today//10
                            b = today%10
                            color[a] += 1
                            color[b] += 1
                        else:
                            color[today] += 1
                i += 1
        return color, color_r

color_r = count_color(today_sun)
color_b, color_r_1 = count_color(today_sat, blue=True)
count = [0] * 10
for i in holi:
    for j in i:
        if j // 10 >= 1:
            a = j//10
            b = j%10
            count[a] += 1
            count[b] += 1
        else:
            count[j] += 1

new = []
for i in range(10):
    tmp = list(map(str, [color_r[i] + color_r_1[i] + count[i], color_b[i], total[i]- (color_r[i] + color_r_1[i]+color_b[i]+count[i])]))
    print(' '.join(tmp))
    new.append(tmp)
# print(new)
print(holi)