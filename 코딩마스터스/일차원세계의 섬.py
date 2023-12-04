import sys, math
input = sys.stdin.readline

nums = [math.ceil(i/2) for i in range(0, 103)]
s = list(input().strip())
new_s_for_max = s.copy()
new_s_for_min = s.copy()
for i in range(1, len(s)-1):
    now = s[i]
    now_2 = new_s_for_min[i]
    if now == 'g':
        if s[i-1] == 'x':
            new_s_for_max[i-1] = 'o'
        if s[i+1] == 'x':    
            new_s_for_max[i+1] = 'o'
    if now_2 == 'g':
        if new_s_for_min[i+1] == 'x':
            new_s_for_min[i+1] = 'g'
            
def count_island(arr,max =True):
    if max: 
        k = ''.join(arr).split( 'o')
        k = [i for i in k if i != '']
        count = 0 
        for i in k:
            if i[0] == 'x':
                count += nums[len(i)]
            else:
                count += 1
    else:
        k = ''.join(arr).replace('x', 'o').split( 'o')
        k = [i for i in k if i != '']
        count = len(k)

    return count

print(count_island(new_s_for_min, False)) 
print(count_island(new_s_for_max)) 


