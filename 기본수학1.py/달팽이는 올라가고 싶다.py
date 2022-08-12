# import sys

# A, B, V = map(int, sys.stdin.readline().split())

# if V == A:
#     day = 0
# elif (V-A) // (A-B) < 1:
#     day = 1
# else:
#     if (V - A) % (A - B) > 0:
#         day = (V - A) // (A - B) + 1
#     else:
#         day = (V - A) // (A - B)

        
# print(day + 1)


climb, fall, height = map(int, input().split(" "))

day = (height - climb) // (climb - fall)
height -= (climb - fall) * day

while True:
    day += 1
    height -= climb
    if height <= 0:
        break
    height += fall

print(day)
