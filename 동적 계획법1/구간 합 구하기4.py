import sys
n, k = map(int, sys.stdin.readline().split())
nums = [0] + list(map(int, sys.stdin.readline().split()))


ans = [0]
for i in range(1, n+1):
    s = ans[-1] + nums[i]
    ans.append(s)
    
for _ in range(k):
    i, j = map(int, sys.stdin.readline().split())
    print(ans[j]- ans[i-1])



## 이중 for루프를 사용하면 시간 초과가 나게 된다.
## 따라서 이를 없앨수 있는 방향으로 풀어야 한다. 
## 미리 누적합을 만들고 주어진 인덱스에 맞는 값을 빼서 
## 인덱스 간의 누적합을 구하는 방법을 사용한다.