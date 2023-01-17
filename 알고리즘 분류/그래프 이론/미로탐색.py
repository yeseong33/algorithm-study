import sys
from collections import deque

n, m = map(int, sys.stdin.readline().split())

maze = [[0]*(m+2)]
for i in range(n):
    k = [0] + list(map(int, sys.stdin.readline().strip())) +[0]
    maze.append(k)
maze.append([0] * (m+2))


visited = [[0] * (m+2) for i in range(n+2)]
ans = m * n + 1


queue = deque([[1, 1, 1]])

while queue:
    node = queue.popleft()
    row = node[0]
    col = node[1]
    count = node[2]
    
    if visited[row][col] == 0:
        visited[row][col] = 1
        
        up = [row-1, col, count+1]
        down = [row+1, col, count+1]
        right = [row, col+1, count+1]
        left = [row, col-1, count+1]
        
        if maze[up[0]][up[1]] == 1 and visited[up[0]][up[1]] == 0:
            queue.append(up)
        if maze[down[0]][down[1]] == 1 and visited[down[0]][down[1]] == 0:
            queue.append(down)
        if maze[right[0]][right[1]] == 1 and visited[right[0]][right[1]] == 0:
            queue.append(right)
        if maze[left[0]][left[1]] == 1 and visited[left[0]][left[1]] == 0:
            queue.append(left)
            
        if row == n and col == m and count < ans:
            ans = count


print(ans)
