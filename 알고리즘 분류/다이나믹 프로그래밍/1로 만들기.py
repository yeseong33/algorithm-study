# n = int(input())
# ans = []
# count = 0 
# a = 10000
# b = 10000
# c = 10000
# def makeOne(n, count):
#     global a,b,c
#     if n == 1:
#         ans.append(count)
#         return count
    
#     if n % 3 == 0:
#         count +=1 
#         a = makeOne(n // 3, count)
#         count -= 1 
#     if n % 2 == 0:
#         count += 1
#         b = makeOne(n//2, count)
#         count -= 1
#     n -= 1
#     count += 1
#     c = makeOne(n, count)
#     count -= 1
    

# makeOne(n, count)
# print(min(ans))


n = int(input())

nums =[0] * (10**6+1)

nums[1] = 1
nums[2] = 1
nums[3] = 1

for i in range(4, n+1):
    if i%6 == 0:
        nums[i] = min (nums[i-1], nums[i//3], nums[i//2])+1
    elif i%3 == 0:
        nums[i] = min (nums[i-1], nums[i//3])+1
    elif i%2 == 0:
        nums[i] = min (nums[i-1], nums[i//2])+1
    else:
        nums[i] = nums[i-1]+1

if n != 1:
    print(nums[n])
else:
    print(0)