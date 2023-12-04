from heapq import heappop, heappush

def bfs(n, k):
    INF = int(10e9) 
    if n > k:
        print(n-k)
        return
    elif n == k:
        print(0)
        return 
    q = []
    heappush(q, n)
    min_count = 2*k 
    visited = [0] * (2*k+3)
    
    while q:
        now = heappop(q)
        if visited[now] > min_count:
            continue
        
        if now == k:
            break
        elif now > k:
            if visited[now]  + now - k < min_count:
                min_count = visited[now] + now - k
            continue
        
        for i in (now+3, now-1, now*2):
            if -3 < i <= 2 * k and not visited[i]:  
                heappush(q, i)
                visited[i] = visited[now] + 1 

    print(min(visited[now], min_count))
                
            
t = input().split()
n, k = int(t[0]), int(t[1])
bfs(n, k)
