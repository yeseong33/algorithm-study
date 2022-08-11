# import sys

# n = int(input())
# con = 0

# for i in range(n):
#     s = sys.stdin.readline()
#     count = 0
#     while s != '':
#         k = s.lstrip(s[0])
#         if k.count(s[0]) > 0:
#             count += 1
#             break
#         s = s.lstrip(s[0])
#     if count == 0:
#         con += 1
# print(con)

s = '1234'
print(s.find('3'))