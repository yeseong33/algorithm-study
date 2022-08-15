import sys

def sosu(n):
    nums = [True for i in range(n+1)]
    nums[0] = False
    nums[1] = False
    for i in range(2, int(n ** 0.5)+1):
        if nums[i]:
            for i in range(2*i, n+1, i):
                nums[i] = False
    so = [i for i in range(len(nums)) if nums[i]]
    return so 


def partition(data):
    ans = []
    sosu = sosu(10000)
    for i in range(len(data)):    
        k = data[i]//2
        a = k
        b = k
        while True:
            if a in sosu and b in sosu:
                if a + b == data[i]:
                    break
            a -= 1
            b += 1 
        ans.append(str(a)+' '+str(b))
    return ans



t = int(sys.stdin.readline())

data = [int(sys.stdin.readline().strip()) for i in range(t)]

p = partition(data)

for i in p:
    print(i)

    
