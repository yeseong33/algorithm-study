from sys import stdin

def run():
    input = stdin.readline
    n = int(input())
    nums = list(map(int, input().split()))
    visited = [0] * n
    for i in range(n):
        visited[i] = 1
        for j in range(n):
            if not visited[j]:
                visited[j] = 1
                for k in range(n):
                    if not visited[k]:
                        visited[k] = 1
                        for l in range(n):
                            if not visited[l]:
                                visited[l] = 1
                                if nums[i] * nums[j] == nums[k] * nums[l]:
                                    print('YES')
                                    return 
                                visited[l] = 0
                        visited[k] = 0
                visited[j] = 0 
        visited[i] = 0 
    print('NO')
run()