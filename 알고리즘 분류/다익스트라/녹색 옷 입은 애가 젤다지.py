# import sys, heapq

# class zelda:
    
#     def __init__(self, d, n, costs, board):
#         self.visited = []
#         self.d = d
#         self.n = n
#         self.costs = costs
#         self.board = board
        
    
#     def dix(self, x, y, c):
#         q = []
#         heapq.heappush(q, (c, x, y))
        
#         while q:
#             cost, x, y = heapq.heappop(q)

#             for i in range(4):
#                 nx = x + self.d[i][0]
#                 ny = y + self.d[i][1]
#                 if 0 <= nx < self.n and 0 <= ny < self.n:
#                     if self.costs[nx][ny] > cost + self.board[nx][ny]:
#                         self.costs[nx][ny] = cost + self.board[nx][ny]
#                         heapq.heappush(q, (self.costs[nx][ny], nx, ny))
        
    
        
        
# INF = int(1e10)
# ii = 0
# while True:
#     ii += 1
#     n = int(input())
    
#     if n == 0:
#         break

#     board = []
#     for i in range(n):
#         k = list(map(int, sys.stdin.readline().split()))
#         board.append(k)
#     d = [(1, 0), (-1, 0),(0, 1), (0, -1)]
#     costs = [[INF] * n for i in range(n)]
#     costs[0][0] = board[0][0]
#     ze = zelda(d, n, costs, board)
#     ze.dix(0, 0, costs[0][0])
#     print("Problem " +str(ii) + ": " + str(ze.costs[n-1][n-1]))
    

a = 'afeaw'
b = a.replace('a', 'b')
print(b )
a = ['2', '3', '5']
k = ''.join(a)
print(k)

t = a.index('2')
print(t)

a = [1,2, 3]
k = [2, 1, 3]
print(a==k)