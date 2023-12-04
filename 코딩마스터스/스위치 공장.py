# from sys import stdin, stdout

# input = stdin.readline

# n = int(input())

# swhich_1_on = False
# swhich_2_on = False
# time = [0, 0, 0, 0]
# times = [(0, 0)]
# acts = [] 

# for i in range(n):
#     t, o = input().split()
#     t = int(t)
#     acts.append((t, o))
# acts.sort(reverse=True)

# q = int(input())
# qs = set({int(input()) for _ in range(q)})

# for t in range(1, max(qs)+1): 
#     if acts != [] and acts[-1][0] == t:
#         t, o = acts.pop()
    
#         if o == 'A' and not swhich_1_on:
#             swhich_1_on = True
#             time[2] = t
#         elif o == 'A' and swhich_1_on:
#             swhich_1_on = False
#             time[0], time[2] = time[0]+t-time[2], 0
#         elif o == 'C':
#             swhich_2_on = True
#             time[3] = t 
#         elif o == 'D':
#             swhich_2_on = False
#             time[1], time[3] = time[1]+ t-time[3], 0
            
#     if not swhich_1_on:
#         a = time[0]
#     else:
#         a = time[0] + t-time[2]
        
#     if not swhich_2_on:
#         b = time[1]
#     else:
#         b = time[1] + t-time[3]
        
#     times.append((a, b))
        
# for i in qs:
#     print(*times[i])
    
from sys import stdin, stdout

input = stdin.readline
print = stdout.write

n = int(input())

swhich_1_on = False
swhich_2_on = False
time = [0, 0, 0, 0]
times = [(0, 0, 0, 0, 0)]

for i in range(n):
    t, o = input().split()
    t = int(t)
    
    if o == 'A' and not swhich_1_on:
        swhich_1_on = True
        time[2] = t
    elif o == 'A' and swhich_1_on:
        swhich_1_on = False
        time[0], time[2] = time[0]+t-time[2], 0
    elif o == 'C':
        swhich_2_on = True
        time[3] = t 
    elif o == 'D':
        swhich_2_on = False
        time[1], time[3] = time[1]+ t-time[3], 0
    a, c = (time[0], 0) if not swhich_1_on else (time[0] + t - time[2], 1)
    b, d = (time[1], 0) if not swhich_2_on else (time[1] + t - time[3], 1)
    times.append([a, b, c, d, t])

q = int(input())
qs = [int(input()) for _ in range(q)]

for t in qs: 
    if t > times[-1][4]:
        now = times[-1]
        plus =  t -now[4]
        if now[2]:
            a = now[0] + plus
        else:
            a = now[0]
        
        if now[3]:
            b = now[1] + plus
        else:
            b = now[1]
   
        print(' '.join(map(str, (a, b, '\n'))))
        continue
    for i in range(1, len(times)):
        status = times[i][4]
        if t < status:
            now = times[i-1]
            plus = t-now[4]
            a = now[0] + plus if now[2] else now[0]
            b = now[1] + plus if now[3] else now[1]

            print(' '.join(map(str, (a, b, '\n'))))
            break
