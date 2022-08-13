import sys

t = int(sys.stdin.readline())
for i in range(t):
    h, w, n = map(int, sys.stdin.readline().split())
    if n % h == 0:
        roomNum = n // h
        roomF= h
    else:
        roomNum = n // h + 1
        roomF= n % h
    room = str(roomF) + str(roomNum).zfill(2)
    print(room)
    