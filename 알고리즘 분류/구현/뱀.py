import sys

n = int(input())

k = int(input())

board = [[0] * (n+1) for i in range(n+1)]

for i in range(k):
    a, b =map(int, sys.stdin.readline().split()) 
    board[a][b] = 1

l = int(input())


for i in range(l):
    k = list(sys.stdin.readline().split())
    move[int(k[0])] = k[1]    
    move.append([int(k[0]), k[1]])

d = [(-1, 0), (0, 1), (1, 0), (0, -1)]

def snake():
    s = [[1, 1]]
    dir = 1
    count = 0

    while count < 10001:
        a, b = s[0][0], s[0][1]
        na = a + d[dir][0]
        nb = b + d[dir][1]
        if 1 <= na < n+1 and 1 <= nb < n+1 and [na, nb] not in s:
            if board[na][nb] == 1:
                s = [[na, nb]] + s
                board[na][nb] = 0
            else:
                s.pop()
                s = [[na, nb]] + s
        else:
            count += 1
            return count
        count += 1
                
        if move[count] != 0:
            if move[count] == 'D':
                dir = (dir + 1) % 4
            else:
                if dir == 0:
                    dir = 3
                else:
                    dir -= 1 
                
    return count

k = snake()
print(k)
        

    
