# number = input('')
# numbers = input('')
# k = numbers.split(' ')
# mini = 1000000
# maxi = -1000000
# for i in k:
#     num = int(i)
#     if num > maxi:
#         maxi = num
#     if num < mini:
#         mini = num
# print(mini, maxi)


import sys


# input()
# # 개수만 받아오는 보여주기식``
# numList = list(map(int, sys.stdin.readline().split()))
# # 라인을 읽어서 int 형식으로 list를 만드어 준다.
# print(numList)
# print(min(numList), max(numList))


# data = []
# n = int(sys.stdin.readline())
# for i in range(n):
#     data += sys.stdin.readline().split()
# print(data)

# data = []
# for i in range(9):
#     data += list(map(int, sys.stdin.readline().split()))
# print(max(data))
# print(data.index(max(data))+1)

data = [int(input()) for i in range(9)]
print(max(data))
print(data.index(max(data))+1)