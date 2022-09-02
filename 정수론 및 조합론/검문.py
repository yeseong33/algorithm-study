import sys, math 

# ## (1) - time over
n = int(sys.stdin.readline())

nums = [int(sys.stdin.readline()) for i in range(n)]

m = []
a = 2
while a <= nums[1]-nums[0]:
    c = 0 
           
    t = nums[0] % a

    for i in nums:
        if t != i % a:
            c += 1
            break
    if c == 0:
        m.append(a)
    
    a += 1
    
for i in m:
    print(i, end = ' ')




# ## (2)
def make(n):
    k = []
    for i in range(2, int(math.sqrt(n))+1):
        if n % i == 0:
            k.append(i)
            if i**2 != n:
                k.append(n//i)
    k.sort()
    k.append(n)            
    return k



n = int(sys.stdin.readline())

nums = [int(sys.stdin.readline()) for i in range(n)]
nums.sort()

mi = []
for i in range(n-1):
    l = nums[i+1]-nums[i]
    mi.append(l)


t = set(make(mi[0]))
for i in mi:
    k = t.intersection(set(make(i)))
    t = k

t = list(t)
t.sort()

for i in t:
    print(i, end = ' ')
    
    